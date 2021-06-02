import boto3
import uuid
import requests
import json

from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from flask import Flask, render_template, request, redirect, url_for, session
application = Flask(__name__)
app = application

# Change these according to your details
variables = {
    "region_name": "us-east-1",
    "aws_access_key_id": "AKIAQMIDYSWEMRZJYWVT",
    "aws_secret_access_key": "IvLXb/dIYL3Bg7p7Z4DCx4HkiodeLWfqhnpC3GpN",
    "api_link": "https://7ugesarq11.execute-api.us-east-1.amazonaws.com/default/processStockData"
}

app.secret_key = "iqFfhY9FCUOJ8Z46DQLDe93mEMBln4W6"
dynamodb_resource = boto3.resource('dynamodb', region_name=variables["region_name"])
dynamodb_client = boto3.client('dynamodb', region_name=variables["region_name"])
lambda_client = boto3.client('lambda', region_name=variables["region_name"])


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
                        'stocks': [],
                        'username': username,
                        'password': password
                    }
                )
                return {'result':True,'message':'Success, Account created.'}
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
def get_change(previous, current):
    if current == previous:
        return 100.0
    try:
        return round(float(((current - previous) * 100) / previous), 2)
    except ZeroDivisionError:
        return 0
def user_add_stock(currency_code, amount_owned):
    db_users = dynamodb_resource.Table('users')
    db_userActivityData = dynamodb_resource.Table('userActivityData')
     
    if db_users:
        db_users.update_item(
            Key={
                'userid': session['userid']
            },
            UpdateExpression="SET stocks = list_append(stocks, :item)",
            ExpressionAttributeValues={
                ':item': [{"amount_owned":amount_owned, "currency_code": currency_code}]
            },
            ReturnValues="UPDATED_NEW"
        )
        
        response = db_userActivityData.put_item(
            Item={
                'dataid': str(uuid.uuid4()),
                'data_type': "stock_bought",
                'currency_code': currency_code,
                'amount': amount_owned
            }
        )
def user_owns_stock(currency_code):
    user = get_user(session['userid'])
    for stock in user['stocks']:
        if stock['currency_code'] == currency_code:
            return True
    return False
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

    if request.method == "POST":
        user = get_user(session['userid'])
        current_password = request.form['current_password']
        desired_password = request.form['desired_password']

        if not current_password:
            return render_template('profile.php', user=user, error_message="Error: Current password field is empty.")

        if not desired_password:
            return render_template('profile.php', user=user, error_message="Error: Desired password field is empty.")

        if user['password'] == current_password:
            auth_changepassword(session['userid'], desired_password)
            return redirect(url_for('profile'))
        else:
            return render_template('profile.php', user=user, error_message="Error, Current password does not match.")
    
    return redirect(url_for('profile'))
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
    position_total = 0
    
    user = get_user(session['userid'])
    
    for item in user['stocks']:
        pricedata = get_pricedata(item['currency_code'])['price_data']
        stock_data['data'].append({
            "currency_code": item['currency_code'],
            "amount_owned": item['amount_owned'],
            "pricedata": pricedata,
            "percentage_change": get_change(float(pricedata['prices'][1]), float(pricedata['prices'][0])),
            "equity": round(float(item['amount_owned']) * float(pricedata['prices'][0]), 2)
        })
        
    for data in stock_data['data']:
        position_total = round(position_total + data["equity"], 2)
    
    db_analytics = dynamodb_resource.Table('userActivityStats')

    _user_analytics = db_analytics.scan()['Items']

    return render_template('dashboard.php', stock_data=stock_data['data'], position_total=position_total, user_analytics=_user_analytics)
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
            return redirect(url_for('dashboard'))

        if not amount_owned:
            return redirect(url_for('dashboard'))
        
        response = requests.get(variables["api_link"] + '?currency_code=' + stock_code)
        
        if response.json()['message'] == 'Currency code not found.':
            return redirect(url_for('dashboard'))

        if user_owns_stock(stock_code):
            return redirect(url_for('dashboard'))
        
        user_add_stock(stock_code, amount_owned)
    
    return redirect(url_for('dashboard'))
# end-add-stock-route



# Close position route
@app.route('/closeposition/<currency_code>', methods=['POST', 'GET'])
def closeposition(currency_code):
    if 'userid' not in session:
        return redirect(url_for('login'))
    
    if user_owns_stock(currency_code):
        user = get_user(session['userid'])
        db_users = dynamodb_resource.Table('users')
        db_userActivityData = dynamodb_resource.Table('userActivityData')

        new_stocks = []

        for stock in user['stocks']:
            if stock['currency_code'] != currency_code:
                new_stocks.append(stock)

        response = db_users.update_item(
            Key={
                'userid': session['userid']
            },
            UpdateExpression="set stocks=:stocks",
            ExpressionAttributeValues={
                ':stocks': new_stocks
            },
            ReturnValues="UPDATED_NEW"
        )

        response = db_userActivityData.put_item(
            Item={
                'dataid': str(uuid.uuid4()),
                'data_type': "stock_sold",
                'currency_code': currency_code
            }
        )
    
    return redirect(url_for('dashboard'))
# end-close-position-route



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



def setup_application():
    # Setup tables with default data / attributes on first start
    existing_tables = dynamodb_client.list_tables()['TableNames']
    if 'users' not in existing_tables:
        dynamodb_resource.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'userid',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'userid',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
    if 'stockData' not in existing_tables:
        dynamodb_resource.create_table(
            TableName='stockData',
            KeySchema=[
                {
                    'AttributeName': 'currency_code',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'currency_code',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
    if 'userActivityData' not in existing_tables:
        dynamodb_resource.create_table(
            TableName='userActivityData',
            KeySchema=[
                {
                    'AttributeName': 'data_type',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'data_type',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
    if 'userActivityStats' not in existing_tables:
            dynamodb_resource.create_table(
                TableName='userActivityStats',
                KeySchema=[
                    {
                        'AttributeName': 'stat_name',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'stat_name',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )

    db_activitystats = dynamodb_resource.Table('userActivityStats')

    result = db_activitystats.scan(FilterExpression=Attr('stat_name').eq('most_purchased'))
    if result["Count"] == 0:
        db_activitystats.put_item(
            Item={
                'stat_name': "most_purchased",
                'stat_data': {}
            }
        )

    result1 = db_activitystats.scan(FilterExpression=Attr('stat_name').eq('highest_moved'))
    if result1["Count"] == 0:
        db_activitystats.put_item(
            Item={
                'stat_name': "highest_moved",
                'stat_data': {}
            }
        )

    result2 = db_activitystats.scan(FilterExpression=Attr('stat_name').eq('most_sold'))
    if result2["Count"] == 0:
        db_activitystats.put_item(
            Item={
                'stat_name': "most_sold",
                'stat_data': {}
            }
        )

setup_application()   
    
        