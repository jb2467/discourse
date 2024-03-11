import hashlib
import secrets
from flask_restful import Resource
from src.db import users_db

from flask_restful import request
from flask_restful import reqparse
import json

class Login(Resource):
    def post(self): 
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        print(username, 'username')
        print(password, 'password')
        exist_password = users_db.get_user_password(username)
        print(exist_password, 'exist_password')
        if(exist_password and exist_password[0][0] == password):
            key = secrets.token_urlsafe(16)
            s = users_db.update_session_key(key,username)
            return {'session_key': key}, 200
        return "Fail", 400
