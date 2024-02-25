import hashlib
from flask_restful import Resource
from src.db import chats_db

from flask_restful import request
from flask_restful import reqparse
import json

class Channel(Resource):
    def put(self):
        return ""
    def get(self):

        return ''
    def delete(self):
       return ""
    def post(self): 
        data = request.get_json()
        username = data.get('username')
        message = data.get('message')
        channel_id = data.get('channel_id')
        chats_db.add_message(username, message, channel_id)
        return '',400
