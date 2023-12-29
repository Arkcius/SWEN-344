import os
import json
from psycopg2.extras import execute_values
from .swen_344_db_utils import *
def populate_db():

    exec_sql_file('nutri.sql')

    with open('server/api/foodDB.json') as json_file:
        data = json.load(json_file)

    for foods in data:
        list_of_tuples = []
        list_of_tuples.append((
            foods['name'],
            foods['category'],
            foods['calories'],
            foods['totalFat'],
            foods['saturatedFat'],
            foods['transFat'],
            foods['protein'],
            foods['carbohydrate']))
        conn = connect()
        cur = conn.cursor()
        sql = "INSERT INTO food(name, category, calories, totalFat, saturatedFat, transFat, protein, carbohydrate) VALUES %s"
        execute_values(cur, sql, list_of_tuples)
        conn.commit()
        conn.close()
    
def update_food(food, data, typeData):
    if(typeData in ['calories', 'totalFat', 'saturatedFat', 'transFat', 'protein', 'carbohydrate']):
        data = float(data)

    sql = """UPDATE food SET %s = '%s' WHERE name = '%s'""" %(typeData, data, food)
    exec_commit(sql)
    return True

def get_food_by_category(category):
    sql = """SELECT * FROM food WHERE category = '%s' ORDER BY id ASC""" %(category)
    result = exec_get_all(sql)
    cat = []
    count = 0
    for food in result:
        cat.append({
            'name' : food[1], 
            'calories' : float(food[3]), 
            'totalFat' : float(food[4]), 
            'saturatedFat' : float(food[5]), 
            'transFat' : float(food[6]), 
            'protein' : float(food[7]), 
            'carbohydrate' : float(food[8])
        })
        count = count + 1
    return cat