import boto3
import uuid # str(uuid.uuid4())

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
        response = db_users.get_item(
            Key={
                'email': email
            }
        )
        if 'Item' in response:
            item = response['Item']
            
            if item['password'] == password:
                session['userid'] = str(item['userid'])
                return {'result':True,'message':'Success.'}
            else:
                return {'result':False,'message':'Password does not match.'}
    else:
        return {'result':False,'message':'DB Error.'}
    
# def auth_register(fullname, username, password, email, phonenumber):
#     db_users = dynamodb_resource.Table('users')
    
#     if db_users:
#         response = db_users.scan(
#             FilterExpression=Attr('username').equals(username) & Attr('email_address').contains(email)
#         )
        
#         print(response['Items'])
#     else:
#         return {'result':False,'message':'DB Error.'}
# end-functions



# Home route
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.php')
# end-home-route


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
        
        return render_template('login.php', error_message=response)
    
    return render_template('login.php')
# end-login-route


# Register route
@app.route('/register/', methods=['POST', 'GET'])
def register():
    return render_template('register.php')
# end-register-route
