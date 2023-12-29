import unittest
from src.library import *
from src.swen344_db_utils import connect

class TestChat(unittest.TestCase):
    def setUp(self):
        exec_sql_file("db-rar6741/tests/librarytest.sql")
    
    def test_build_tables(self):
        """Build the tables"""
        rebuildTables()
        result = exec_get_all('SELECT * FROM users')
        self.assertEqual([], result, "no rows in users")

    def test_rebuild_tables_is_idempotent(self):
      """Drop and rebuild the tables twice"""
      rebuildTables()
      rebuildTables()
      result = exec_get_all('SELECT * FROM users')
      self.assertEqual([], result, "no rows in users")

    #tests to make sure amount of rows is correct when created
    def test_rows_users(self):
        result = getUsers()
        self.assertEqual(len(result),4,"number of rows should be 4")
    def test_rows_type(self):
        result = getTypes()
        self.assertEqual(len(result),2,"number of rows should be 2")
    def test_rows_inventory(self):
        result = getBooks()
        self.assertEqual(len(result),6,"number of rows should be 6")
    def test_rows_checkedout(self):
        result = getUserCheckouts()
        self.assertEqual(len(result),6,"number of rows should be 6")

    #makes sure arts check outs is zero
    #test case given
    def test_art_empty(self):
        result = getUserCheckout("Art Garfunkel")
        self.assertEqual(len(result),0,"Number of books for art should be 0")

    #tests to see all of jackies checkouts sorted by book name
    #test case given
    def test_jackie_checkout(self):
        expected = "[('Jackie Gleason', 'Book', datetime.date(2023, 9, 10), None), ('Jackie Gleason', 'Book5', datetime.date(2023, 10, 10), datetime.date(2023, 10, 23)), ('Jackie Gleason', 'Kare', datetime.date(2021, 8, 10), datetime.date(2021, 10, 23))]"
        self.assertEqual(str(getUserCheckout("Jackie Gleason")),expected,"Number of books for jackie should be 3")

    #tests to see all users check outs sorted by username
    #test case given
    def test_list_checkout(self):
        expected = "[('Ada Lovelace', 'Kare'), ('Ada Lovelace', 'Book1'), ('Jackie Gleason', 'Book5'), ('Jackie Gleason', 'Kare'), ('Jackie Gleason', 'Book'), ('Mary Shelley', 'Book4')]"
        self.assertEqual(str(getUserCheckouts()),expected,"number of checkouts should be 6")

    #checks that all info for ada given when checking her info
    def test_check_ada_info(self):
        expected = "[(1, 'Ada Lovelace', 'ada@gmail.com', True)]"
        self.assertEqual(expected, str(getUser("Ada Lovelace")))

    #checks to make sure all data for book 3 is gotten and correct
    def test_check_book3_info(self):
        expected = "[(3, 'Book3', 'Ryan', '09/10/2023', 10, 1, None, None)]"
        self.assertEqual(expected, str(getBooktitle("Book3")))

    #gets all books of nonfiction type and all theyre info including quantity
    #test case given
    def test_check_book_type(self):
        expected = "[('Book4', 5), ('Book5', 6), ('Book', 0)]"
        self.assertEqual(expected, str(getBookType(2)))

    #gets all books currently in inventory to check if theyre correct
    def test_get_books(self):
        expected = "[(1, 'Book1', 'Ry', '09/10/2023', 4, 1, None, None), (2, 'Kare', 'Ryl', '09/10/2023', 3, 1, None, None), (3, 'Book3', 'Ryan', '09/10/2023', 10, 1, None, None), (4, 'Book4', 'bob', '09/10/2023', 5, 2, None, None), (5, 'Book5', 'car', '09/10/2023', 6, 2, None, None), (6, 'Book', 'tim', '09/10/2023', 0, 2, None, None)]"
        self.assertEqual(expected, str(getBooks()))
    
    #gets all current types and sees if they are correct
    def test_get_types(self):
        expected = "[(1, 'Fiction'), (2, 'Non-Fiction')]"
        self.assertEqual(expected,str(getTypes()))
    
    #tests if adding 2 new users works
    #test case given
    def test_add_new_user(self):
        addUser("Christopher Marlowe","chris@gmail.com")
        addUser("Francis Bacon","fran@gmail.com")
        expected = "[(5, 'Christopher Marlowe', 'chris@gmail.com', True)]"
        expected2 = "[(6, 'Francis Bacon', 'fran@gmail.com', True)]"
        self.assertEqual(expected,str(getUser("Christopher Marlowe")))
        self.assertEqual(expected2,str(getUser("Francis Bacon")))
    #tests deleteing a user
    def test_delete_user(self):
        deactivateUser("Ada Lovelace")
        expected = "[(1, 'Ada Lovelace', 'ada@gmail.com', False)]"
        self.assertEqual(expected,str(getUser("Ada Lovelace")))

    #searches for how many copies of a book then deletes
    #test case given
    def test_check_for_book_and_delete(self):
        addBook("The Last Man","ME","09/22/2021",0,1)
        if getBooksCopies("Book") == 0:
            deactivateUser("Mary Shelley")
        expected = "[(2, 'Mary Shelley', 'mary@gmail.com', False)]"
        expected2 = "[(7, 'The Last Man', 'ME', '09/22/2021', 0, 1, None, None)]"
        self.assertEqual(expected,str(getUser("Mary Shelley")))
        self.assertEqual(expected2,str(getBooktitle("The Last Man")))

    
    #test checkout where book goes on reserve
    #test case given
    def test_checkout_reserve(self):
        checkout("Jackie Gleason","Book","Henrietta","9/17/2023")
        expected=("[('Jackie Gleason', 'Book', True)]")
        self.assertEqual(expected,str(getUserReserve("Jackie Gleason")))

    #test to see if normal checkout works
    def test_checkout(self):
        checkout("Jackie Gleason","Book3","Fairport","9/17/2023")
        expected=("[('Jackie Gleason', 'Book', datetime.date(2023, 9, 10), None), ('Jackie Gleason', 'Book3', datetime.date(2023, 9, 17), None), ('Jackie Gleason', 'Book5', datetime.date(2023, 10, 10), datetime.date(2023, 10, 23)), ('Jackie Gleason', 'Kare', datetime.date(2021, 8, 10), datetime.date(2021, 10, 23))]")
        self.assertEqual(expected,str(getUserCheckout("Jackie Gleason")))
    
    #gets all book checkouts orderd by type and author
    #test case given
    def test_book_checkout(self):
        result = getBookCheckouts()
        expected = "[('Ada Lovelace', 'Book1', datetime.date(2041, 9, 10), None, 4), ('Ada Lovelace', 'Kare', datetime.date(2021, 9, 10), None, 3), ('Jackie Gleason', 'Kare', datetime.date(2021, 8, 10), datetime.date(2021, 10, 23), 3), ('Mary Shelley', 'Book4', datetime.date(2021, 9, 10), None, 5), ('Jackie Gleason', 'Book5', datetime.date(2023, 10, 10), datetime.date(2023, 10, 23), 6), ('Jackie Gleason', 'Book', datetime.date(2023, 9, 10), None, 0)]"
        self.assertEqual(expected,str(result))

    #tests return book function
    def test_return_book(self):
        addBook("Frankenstein","ME","09/22/2021",3,1)
        addCopiesToLibrary("Henrietta","Frankenstein",2)
        checkout("Art Garfunkel", "Frankenstein","Henrietta","09/22/2022")
        returnBook("Art Garfunkel", "Frankenstein","09/25/2022")
        expected = "[('Art Garfunkel', 'Frankenstein', datetime.date(2022, 9, 22), datetime.date(2022, 9, 25))]"
        expected2 = "3"
        self.assertEqual(expected,str(getUserCheckout("Art Garfunkel")))
        self.assertEqual(expected2,str(getBooksCopies("Frankenstein")))
    
    #test load csv
    def test_load_csv(self):
        loadFile("db-rar6741/tests/Library.csv")
        self.assertEqual(25,len(getBooks()))

    #test case given
    def test_GOT_Case(self):
        #adding book and copies to library
        addBook("The Winds of Winter","George R.R. Martin","10/24/2021",6,1)
        addCopiesToLibrary("Fairport","The Winds of Winter",1)
        addCopiesToLibrary("Towns of Penfield","The Winds of Winter",1)
        addCopiesToLibrary("Henrietta","The Winds of Winter",1)
        addCopiesToLibrary("Pittsford","The Winds of Winter",1)

        checkout("Mary Shelley","The Winds of Winter","Fairport","01/02/2023")
        returnBook("Mary Shelley","The Winds of Winter","01/10/2023")
        checkout("Ada Lovelace","The Winds of Winter","Fairport","01/13/2023")
        makeOverdue("Ada Lovelace","The Winds of Winter")
        checkout("Ada Lovelace","Book3","Fairport","01/28/2023")
        self.assertEqual(len(getUserCheckout("Ada Lovelace")),3)
        returnBook("Ada Lovelace","The Winds of Winter","01/31/2023")
        self.assertEqual(len(checkLateUser("Ada Lovelace")),0)
        checkout("Jackie Gleason","The Winds of Winter","Fairport","03/01/2023")
        returnBook("Jackie Gleason","The Winds of Winter","03/31/2023")
        self.assertEqual(len(getUserCheckout("Jackie Gleason")),4)
        self.assertEqual(len(checkLateUsers()),0)
    #test case given
    def test_good_Samaritan(self):
        addBook("The Winds of Winter","George R.R. Martin","10/24/2021",6,1)
        addCopiesToLibrary("Fairport","The Winds of Winter",3)
        self.assertEqual(getLocalCopies("The Winds of Winter","Fairport"),3)
    #test case given
    def test_Wine_Samaritan(self):
        addBook("The Wines of Winter","WineExpress","10/24/2021",7,1)
        addCopiesToLibrary("Henrietta","The Wines of Winter",2)
        addCopiesToLibrary("Pittsford","The Wines of Winter",2)
        self.assertEqual(getLocalCopies("The Wines of Winter","Henrietta"),2)
        self.assertEqual(getLocalCopies("The Wines of Winter","Pittsford"),2)
    #test case given
    def test_GetAll(self):
        result = getAllLocal()
        self.assertEqual(str(getAllLocal()),"[('Fairport', 'Book3', 3), ('Henrietta', 'Book', 0), ('Henrietta', 'Book5', 2), ('Pittsford', 'Book1', 3), ('Towns of Penfield', 'Book1', 2), ('Towns of Penfield', 'Kare', 3)]")
    
    #need to add test cases for db4 but have the library.py part done
    def test_return_fee(self):
        days,fee = returnBook("Jackie Gleason","Book","09/30/2023")
        print("Days late: "+str(days)+"$"+str(fee))
        self.assertEqual(fee,0.25)
