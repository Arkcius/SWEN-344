from flask_restful import Resource, request,reqparse
from db import methods

class Users(Resource):
    def get(self):
        return methods.list_users()
    
    def delete(self):
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        session = request.headers.get('session')
        ret = methods.deleteUser(firstname,lastname,session)
        if(ret == True):
            return ret
        else:
            print("conflict")
            return False
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstname',type = str)
        parser.add_argument('lastname',type = str)
        parser.add_argument('contact',type = str)
        parser.add_argument('password',type = str)
        args = parser.parse_args()
        ret = methods.addUser(args['firstname'],args['lastname'],args['contact'],args['password'])
        if(ret == True):
            return ret
        else:
            print("conflict")
            return False
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',type = int)
        parser.add_argument('firstname',type = str)
        parser.add_argument('lastname',type = str)
        parser.add_argument('contact',type = str)
        parser.add_argument('password',type = str)
        args = parser.parse_args()
        ret = methods.updateUser(args['id'],args['firstname'],args['lastname'],args['contact'],args['password'])
        if(ret == True):
            return True
        else:
            print("conflict")
            return False

class UserLogin(Resource):
    def get(self):
        firstname = request.args.get('firstname')
        pas = request.args.get('pas')
        ret = methods.loginUser(firstname,pas)
        if(ret == False):
            print("Failed Login")
            return ""
        else:
            return ret

class Books(Resource):
    
    def get(self):
        genre = request.args.get('genre')
        title = request.args.get('title')
        author = request.args.get('author')
        return methods.list_books(genre,author,title)
    
class Checkout(Resource):
    def get(self):
        return methods.getCheckouts()
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title',type = str)
        parser.add_argument('reserve',type = bool)
        session = request.headers.get('session')
        args = parser.parse_args()
        ret = methods.Checkout(args['title'],session,args['reserve'])
        return ret