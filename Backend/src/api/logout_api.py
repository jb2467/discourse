import hashlib
from flask_restful import Resource
from src.db import users_db

from flask_restful import request
from flask_restful import reqparse
import json


class LogOut(Resource):
    def put(self, username):
        users_db.update_session_key('',username)
        return 'Logged', 200
    