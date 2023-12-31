from flask import Flask
from flask_restful import Resource, Api
from api.hello_world import HelloWorld
from api.management import *
from api.methodcalls import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Init, '/manage/init') #Management API for initializing the DB

api.add_resource(Version, '/manage/version') #Management API for checking DB version

api.add_resource(HelloWorld, '/') 

api.add_resource(Users, '/users') 
api.add_resource(UserLogin, '/users/login') 

api.add_resource(Books, '/books') 


api.add_resource(Checkout, '/checkout') 


if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True)