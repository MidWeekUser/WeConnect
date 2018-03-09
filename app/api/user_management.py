import uuid
from flask import Flask, jsonify, request
from flask_restplus import Resource, Api, fields
try:
    from app.models import UserManagement, BusinessManagement
except Exception:
    from WeConnect.app.models import UserManagement, BusinessManagement

user_data = []
# login_info = []
userid = uuid.uuid1
UserObj = UserManagement()

class RegisterUsers(Resource):
    
    def post(self):
        
        user_data = request.json
        user_id = userid
        email = user_data['email']
        firstname = user_data['firstname']
        secondname = user_data['secondname']
        username = user_data['username']
        password = user_data['password']
        confirmpassword = user_data['confirmpassword']

        status = UserObj.registernewuser(user_id, email, firstname, secondname, username, password, confirmpassword)
        
        return status
    
    def get(self):
        response = []
        for user in UserObj.user_data:
            response.append(user.todict())
        return jsonify(response)


class LogInUsers(Resource):
    def post(self):
        return {'Alert': 'Post Successful'}, 201
    def get(self):
        return {'Alert': 'Get Successful'}, 200


    