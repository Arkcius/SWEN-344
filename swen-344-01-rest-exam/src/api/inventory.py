from flask_restful import Resource, request, reqparse
from db.swen344_db_utils import *

class Inventory(Resource):
#get handles a variety of parameters.  Parameters are sent as query strings
#There can be zero or one (single) argument
#If there is an argument, it is used to filter the query
#e.g. ?type={somevalue}, where {somevalue} ... without the {} ... is the filter value applied to 'type'
    def get(self):
        firstname = request.args.get('firstname')
        if firstname== None:
            return exec_get_all("""SELECT manufacturer.name, inventory.model, ev_type.type, inventory.description, inventory.quantity FROM inventory
                                INNER JOIN ev_type on inventory.type_id = ev_type.id
                                INNER JOIN manufacturer on inventory.manf_id = manufacturer.id
                                """)
        elif firstname!= None:
            return exec_get_all("""SELECT manufacturer.name, inventory.model, ev_type.type, inventory.description, inventory.quantity FROM inventory
                                INNER JOIN ev_type on inventory.type_id = ev_type.id
                                INNER JOIN manufacturer on inventory.manf_id = manufacturer.id
                                WHERE inventory.firstname = %s""",firstname)
#post handles new additions to the data.  All data is sent in the body of the HTTP command
#The client sends the required parameters as strings in the json body.  If any foreign keys are needed
#the server (this code) handles getting those keys
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('manufacturer',type = str)
        parser.add_argument('type',type = str)
        parser.add_argument('model',type = str)
        parser.add_argument('description',type = str)
        parser.add_argument('quantity',type = int)
        args = parser.parse_args()
        evtype = exec_get_one('SELECT id FROM ev_type where type = \''+args['type']+'\'')
        manu = exec_get_one('SELECT id FROM manufacturer where name =\''+args['manufacturer']+'\'')
        print(manu)
        exec_commit('INSERT INTO inventory(MANF_ID, MODEL, TYPE_ID, DESCRIPTION, QUANTITY) VALUES(%s,\'%s\',%s,\'%s\',%s)' % (str(manu[0]),args['model'],str(evtype[0]),args['description'],str(args['quantity'])))
        return True
        #Your code goes here

#put handles updates to the data.  All data is sent in the body of the HTTP command
#The client sends the required parameters as strings.
#The server code (here) is responsible for getting the corresponding IDs (as needed) to 
#perform the command
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('manufacturer',type = str)
        parser.add_argument('type',type = str)
        parser.add_argument('model',type = str)
        parser.add_argument('description',type = str)
        args = parser.parse_args()
        id = exec_get_one('SELECT id FROM inventory where type = \''+args['type']+'\'')
        exec_commit('UPDATE inventory SET description = \'%s\', model = \'%s\' WHERE id = %s' %(args['description'],args['model'],str(id[0])))
        return True
        #Your code goes here

#Used to completely remove a model from the inventory
    def delete(self):
        print("delete")
        #Your code goes here
