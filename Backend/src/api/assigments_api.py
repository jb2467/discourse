import hashlib
from flask_restful import Resource
from src.db import assignments_db, course_db

from flask_restful import request
from flask_restful import reqparse
import json

class Assigment(Resource):
    def put(self):
        return ""
    def get(self):
        #?username=student1&course=CSCI140&section=1
        username = request.args.get('username')
        course_code = request.args.get('course_code')
        section_code= request.args.get('section_code')
        data = (username,course_code,section_code)
        return assignments_db.get_assignments(data);
    def delete(self):
       return ""
    def post(self): 
        data = request.get_json()
        assignment_name = data.get('assignment_name')
        course_code = data.get('course_code')
        section_code = data.get('section_code')
        assignments_db.add_assignment(assignment_name,course_code,section_code)
        return "Assignement posted", 200