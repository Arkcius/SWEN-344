from flask_restful import Resource

from flask_restful import request
from flask_restful import reqparse
import json
from .swen_344_db_utils import *
from .helpers import *

parser = reqparse.RequestParser()

class nutriapi(Resource):
    def get(self):
       cat = request.args.get('category')
       print(cat)
       return get_food_by_category(cat)

    def put(self):
        foodname = request.form['foodname']
        dataN = request.form['data']
        typeN = request.form['type']
        result = update_food(foodname, dataN, typeN)
        if(result):
            return True
        return False
    
    