import hashlib
from flask_restful import Resource
from src.db import server_db

from flask_restful import request
from flask_restful import reqparse
import json

class Server(Resource):
    def put(self):
        return ""
    def get(self, server_name):
        return server_db.get_server_channels(server_name);
    def delete(self):
       return ""
    def post(self): 
        return ""
