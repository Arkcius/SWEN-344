import unittest
from src.swen344_db_utils import *

class TestPostgreSQL(unittest.TestCase):
    def setUp(self):
        exec_sql_file("db-rar6741/tests/librarytest.sql")

    def test_can_connect(self):
        result = exec_get_one('SELECT VERSION()')
        self.assertTrue(result[0].startswith('PostgreSQL'))
    
    def test_build_tables(self):
        """Build the tables"""
        result = exec_get_all('SELECT * FROM USERS')
        self.assertEqual(len(result),4, "number of rows should be 4")
        

if __name__ == '__main__':
    unittest.main()