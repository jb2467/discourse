from src.api.db_ultil import exec_sql_file
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)  # create Flask instance
CORS(app)  # Enable CORS on Flask server to work with Nodejs pages
api = Api(app)  # api router

#api.add_resource()


if __name__ == '__main__':
    exec_sql_file('db/database.sql')
    app.run(debug=True, port=4999),
