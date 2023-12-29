from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from api.swen_344_db_utils import *
from api.nutriapi import *
from api.helpers import *

app = Flask(__name__) #create Flask instance

CORS(app)

api = Api(app) #api router

api.add_resource(nutriapi,'/food')

if __name__ == '__main__':
    print("Loading db")
    populate_db()
    print("Starting flask")
    app.run(debug=True), #starts Flask