import boto3
import uuid # str(uuid.uuid4())

from flask import Flask, render_template, request, redirect, url_for, session
application = Flask(__name__)
app = application
app.secret_key = "iqFfhY9FCUOJ8Z46DQLDe93mEMBln4W6"

dynamodb_resource = boto3.resource('dynamodb', region_name='us-east-1')

# Functions
# def login(username, password):
#     if 'userid' in session:
#         return {'result':False,'message':'You are already logged-in.'}
    
#     db_users = dynamodb_resource.Table('users')
    
#     if db_users:
#         response = db_users.get_item(
#             Key={
#                 'username': username
#             }
#         )
#         if 'Item' in response:
#             item = response['Item']
            
#             if item['password'] == password:
#                 session['userid'] = str(item['userid'])
#                 return {'result':True,'message':'Success.'}
#             else:
#                 return {'result':False,'message':'Password does not match.'}
#     else:
#         return {'result':False,'message':'DB Error.'}
# def register(username, password, email, phonenumber):
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
@app.route('/')
def home():
    return render_template('home.php')
# end-home-route
