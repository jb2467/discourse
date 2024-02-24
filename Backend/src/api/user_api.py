import hashlib
from flask_restful import Resource
from src.db import users_db

from flask_restful import request
from flask_restful import reqparse
import json

class Users(Resource):
    def put(self):
        return ""
    def get(self):
        return users_db.get_users();
    def delete(self):
       return ""
    def post(self): 
        id  = len(users_db.get_users()) + 1
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = hashlib.sha512(bytes(data.get('password'), 'ascii')).hexdigest() 
        user = (users_db.get_user(username,email))
        if len(user)>0:
            return '',400
        users_db.add_user((id, username,password,email, ''))
        return  '' ,200
