from src.api.chats_api import Chats
from src.api.user_api import Users

from src.api.login_api import Login
from src.api.logout_api import LogOut
from src.api.db_ultil import exec_sql_file
from src.api.course_api import Course
from src.api.assigments_api import Assigment
from src.api.server_api import Server
from src.api.channels_api import Channel

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from flask import request

app = Flask(__name__)  # create Flask instance
CORS(app)  # Enable CORS on Flask server to work with Nodejs pages
api = Api(app)  # api router

api.add_resource(Users, '/users')
api.add_resource(Login, '/login')
api.add_resource(LogOut, '/logout/<username>')
api.add_resource(Course, '/course/<username>')
api.add_resource(Assigment, '/assignments')
api.add_resource(Server, '/server/<server_name>')
api.add_resource(Channel, '/channel')
api.add_resource(Chats, '/chats')



if __name__ == '__main__':
    exec_sql_file('db/database.sql')
    app.run(debug=True, port=4999),
