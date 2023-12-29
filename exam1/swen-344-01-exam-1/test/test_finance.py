import unittest
from src.finance import *
from src.swen344_db_utils import connect

class TestExam(unittest.TestCase):
    def setUp(self):
        """Setup: This will run automatically before EVERY test"""
        rebuildTables()
        print("Setup done")

    def test_tables(self):
        """Check existence of the tables"""
        print("Question-0: Testing Tables")
        result = exec_get_all('SELECT COUNT(*) FROM DEPT')
        self.assertEqual(3, result[0][0], "Incorreect number of rows in DEPT table")
        result = exec_get_all('SELECT COUNT(*) FROM FACULTY')
        self.assertEqual(26, result[0][0], "Incorrect number of rows in FACULTY table")
        print("Test_tables done")

    def test_q1(self):
        result = question1()
        printResults(result,8,1)
        self.assertEqual(len(result),26)

    def test_q2(self):
        addNew("John","Watson","Biology","Adjunct","1899-04-01","2100")
        result = question1()
        printResults(result,8,2)
        self.assertEqual(len(result),27)

    def test_q3(self):
        ModifyContractEnd("Sherlock","Holmes","1893-12-15")
        result = GetContracts()
        printResults(result,5,3)
        self.assertEqual(len(result),26)

    def test_q4(self):
        result = getFacultyDate(2021)
        printResults(result,8,4)
        self.assertEqual(len(result),8)