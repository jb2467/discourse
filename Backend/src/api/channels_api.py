import hashlib
from flask_restful import Resource
from src.db import server_db

from flask_restful import request
from flask_restful import reqparse
import json

class Channel(Resource):
    def put(self):
        return ""
    def get(self):
        server_name = request.args.get('server_name')
        channel_name = request.args.get('channel_name')
        return server_db.get_messages(server_name, channel_name);
    def delete(self):
       return ""
    def post(self): 
        return ""
