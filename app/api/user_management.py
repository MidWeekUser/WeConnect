from flask import Flask, jsonify, request
from flask_restplus import Resource, Api, fields
try:
    from app.models import UserManagement
except Exception:
    from WeConnect.app.models import UserManagement


user_data = []
# login_info = []


UserObj = UserManagement()

class RegisterUsers(Resource):
    
    
    
    def post(self):
        
        user_data = request.json
        email = user_data['email']
        firstname = user_data['firstname']
        secondname = user_data['secondname']
        username = user_data['username']
        password = user_data['password']
        confirmpassword = user_data['confirmpassword']

        status = UserObj.registernewuser(email, firstname, secondname, username, password, confirmpassword)
        
        return status
    
    def get(self):
        response = []
        for user in UserObj.user_data:
            response.append(user.todict())
        return response

class LogInUsers(Resource):
    def post(self):
        return {'Alert': 'Post Successful'}
    def get(self):
        return {'Alert': 'Get Successful'}

class RegisterNewBusiness(Resource):
    def post(self):
        return {'Alert': 'Post Successful'}
    

# class Login(Resource):
#     from app.models import UserManagement
#     #@api.expect(logininfo)
#     def post(self):
#         #login_info.append(api.payload)
#         login_info.append(logininfo)
#         return login_info
