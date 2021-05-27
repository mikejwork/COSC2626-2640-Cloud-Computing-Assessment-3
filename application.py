import boto3
import uuid # str(uuid.uuid4())
import json

from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from flask import Flask, render_template, request, redirect, url_for, session
application = Flask(__name__)
app = application
app.secret_key = "iqFfhY9FCUOJ8Z46DQLDe93mEMBln4W6"
dynamodb_resource = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id="AKIAQMIDYSWEMRZJYWVT", aws_secret_access_key="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")

# Functions
def auth_login(email, password):
    if 'userid' in session:
        return {'result':False,'message':'You are already logged-in.'}
    
    db_users = dynamodb_resource.Table('users')
    
    if db_users:
        response = db_users.scan(
            FilterExpression=Attr('email').eq(email)
        )
        if response['Count'] == 0:
            return {'result':False,'message':'Email not found, Please try again.'}
        else:
            if response['Items'][0]['password'] == password:
                store_cookies(response['Items'][0])
                return {'result':True,'message':'Success.'}
            else:
                return {'result':False,'message':'Password does not match, Please try again.'}
    else:
        return {'result':False,'message':'DB Error.'}
def auth_register(fullname, username, password, email, phonenumber):
    if 'userid' in session:
        return {'result':False,'message':'You are already logged-in.'}
    
    db_users = dynamodb_resource.Table('users')
    
    if db_users:
        email_check = db_users.scan(
            FilterExpression=Attr('email').eq(email)
        )
        if email_check['Count'] != 0:
            return {'result':False,'message':'Email already exists, Please try again.'}
        else:
            username_check = db_users.scan(
                FilterExpression=Attr('username').eq(username)
            )
            if username_check['Count'] != 0:
                return {'result':False,'message':'Username already exists, Please try again.'}
            else:
                db_users.put_item(
                    Item={
                        'userid': str(uuid.uuid4()),
                        'email': email,
                        'fullname': fullname,
                        'phonenumber': phonenumber,
                        'username': username,
                        'password': password
                    }
                )
                return {'result':True,'message':'Success, Account created.'}
    else:
        return {'result':False,'message':'DB Error.'}
    
    
    
    
    
    if db_users:
        response = db_users.scan(
            FilterExpression=Attr('username').equals(username) & Attr('email_address').contains(email)
        )
        
        print(response['Items'])
    else:
        return {'result':False,'message':'DB Error.'}
def auth_changepassword(userid, new_password):
    db_users = dynamodb_resource.Table('users')
    
    if db_users:
        response = db_users.update_item(
            Key={
                'userid': userid
            },
            UpdateExpression="set password=:password",
            ExpressionAttributeValues={
                ':password': new_password
            },
            ReturnValues="UPDATED_NEW"
        )
def get_user(userid):
    db_users = dynamodb_resource.Table('users')
    
    response = db_users.scan(
        FilterExpression=Attr('userid').contains(str(userid))
    )
    if response['Items']:
        return response['Items'][0]
    else:
        return 'nil'
def store_cookies(item):
    session['userid'] = str(item['userid'])
def clear_cookies():
    session.pop('userid', None)
def get_pricedata(currency_code):
    db_stockdata = dynamodb_resource.Table('stockData')
    response = db_stockdata.scan(FilterExpression=Attr('currency_code').eq(currency_code))
    if response['Count'] == 0:
        return "nil"
    else:
        return response['Items'][0]
def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0
# end-functions



# Home route
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.php')
# end-home-route



# Profile route
@app.route('/profile/', methods=['POST', 'GET'])
def profile():
    if 'userid' not in session:
        return redirect(url_for('login'))
    
    user = get_user(session['userid'])
    
    return render_template('profile.php', user=user)
# end-profile-route



# Change password route
@app.route('/changepassword/', methods=['POST', 'GET'])
def changepassword():
    if 'userid' not in session:
        return redirect(url_for('login'))
    
    user = get_user(session['userid'])
    
    return redirect(url_for('login'))
# end-change-password-route



# Login route
@app.route('/login/', methods=['POST', 'GET'])
def login():
    if 'userid' in session:
        return redirect(url_for('home'))
    
    if request.method == "POST":
        form_email = request.form['email_field']
        form_password = request.form['password_field']
        
        if not form_email:
            return render_template('login.php', error_message="Error: Email field is empty.")

        if not form_password:
            return render_template('login.php', error_message="Error: Password field is empty.")
        
        response = auth_login(form_email, form_password)
        
        if response['result'] == False:
            return render_template('login.php', error_message=response['message'])
        else:
            return redirect(url_for('home'))
    
    return render_template('login.php')
# end-login-route



# Logout route
@app.route('/logout/', methods=['POST', 'GET'])
def logout():
    if 'userid' in session:
        clear_cookies()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# end-logout-route



# Dashboard route
@app.route('/dashboard/', methods=['POST', 'GET'])
def dashboard():
    if 'userid' not in session:
        return redirect(url_for('login'))
    
    stock_data = {"data":[]}
    user = get_user(session['userid'])
    
    
    for item in user['stocks']:
        pricedata = get_pricedata(item['currency_code'])['price_data']
        stock_data['data'].append({
            "currency_code": item['currency_code'],
            "amount_owned": item['amount_owned'],
            "pricedata": pricedata,
            "percentage_change": round(get_change(float(12.13), float(55.23)), 2),#round(get_change(float(pricedata['prices'][0]), float(pricedata['prices'][1])), 2),
            "equity": round(float(item['amount_owned']) * float(pricedata['prices'][0]), 2)
        })
    
    
    
    return render_template('dashboard.php', stock_data=stock_data['data'])
# end-dashboard-route



# Add stock route
@app.route('/addstock/', methods=['POST', 'GET'])
def addstock():
    if 'userid' not in session:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        stock_code = request.form['stock_code']
        amount_owned = request.form['amount_owned']
        
        if not stock_code:
            return render_template('dashboard.php')

        if not amount_owned:
            return render_template('dashboard.php')
    
    return render_template('dashboard.php')
# end-add-stock-route



# Register route
@app.route('/register/', methods=['POST', 'GET'])
def register():
    if 'userid' in session:
        return redirect(url_for('home'))
    
    if request.method == "POST":
        form_email = request.form['email_field']
        fullname_field = request.form['fullname_field']
        username_field = request.form['username_field']
        phonenumber_field = request.form['phonenumber_field']
        form_password = request.form['password_field']
        
        if not form_email:
            return render_template('register.php', error_message="Error: Email field is empty.")
        
        if not fullname_field:
            return render_template('register.php', error_message="Error: Full name field is empty.")
        
        if not username_field:
            return render_template('register.php', error_message="Error: Username field is empty.")
        
        if not phonenumber_field:
            return render_template('register.php', error_message="Error: Phonenumber field is empty.")

        if not form_password:
            return render_template('register.php', error_message="Error: Password field is empty.")
        
        response = auth_register(fullname_field, username_field, form_password, form_email, phonenumber_field)
        
        if response['result'] == False:
            return render_template('register.php', error_message=response['message'])
        else:
            return redirect(url_for('login'))
    
    return render_template('register.php')
# end-register-route
