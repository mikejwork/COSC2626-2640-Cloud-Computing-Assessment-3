#import boto3
#mport uuid # str(uuid.uuid4())

from flask import Flask #, render_template, request, redirect, url_for, session
application = Flask(__name__)
# app.secret_key = "iqFfhY9FCUOJ8Z46DQLDe93mEMBln4W6"

#dynamodb_resource = boto3.resource('dynamodb')

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

# Classes
# class user:
#     userid = None
#     username = None
# end-classes



# Home route
@application.route('/', methods=['POST', 'GET'])
def home():
    
    return 'yoooooooooosdasdjhauihfuhasf'
# end-home-route



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)