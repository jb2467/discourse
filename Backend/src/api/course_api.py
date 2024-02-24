import hashlib
from flask_restful import Resource
from src.db import course_db

from flask_restful import request
from flask_restful import reqparse
import json

class Course(Resource):
    def put(self):
        return ""
    def get(self):
        return course_db.get_courses();
    def delete(self):
       return ""
    def post(self): 
        return ""
