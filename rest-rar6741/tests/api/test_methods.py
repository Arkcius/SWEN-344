import json
import unittest
from tests.test_utils import *


class TestExample(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')
        print("DB Should be reset now")

    def test_users(self):
        expected = [[1, 'Ada', 'Lovelace', 'ada@gmail.com', None, None],[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None],[3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None],[4, 'Art', 'Garfunkel', 'art@gmail.com', None, None]]
        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(expected, actual)

    def test_books(self):
        expected = [[1, 'Hobbit', 'LOTR guy', 'Fiction'], [2, 'Land Before Time', 'dinosaurs', 'Non-Fiction'], [3, 'Library rest', 'Api', 'Non-Fiction'], [4, 'a book', 'a dude', 'Fiction']]
        actual = get_rest_call(self, 'http://localhost:5000/books')
        self.assertEqual(expected, actual)
    
    def test_books_specific(self):
        expected = [[1, 'Hobbit', 'LOTR guy', 'Fiction'], [4, 'a book', 'a dude', 'Fiction']]
        actual = get_rest_call(self, 'http://localhost:5000/books?genre=Fiction')
        self.assertEqual(expected, actual)

    def test_books_specific_multi(self):
        expected = [[2,"Land Before Time","dinosaurs","Non-Fiction"]]
        actual = get_rest_call(self, 'http://localhost:5000/books?genre=Non-Fiction&author=dinosaurs')
        self.assertEqual(expected, actual)
#rest 2 cases start here but the book list cases are Above as i had them from rest 1
    #adding user
    def test_add_user(self):
        expected = [[1, 'Ada', 'Lovelace', 'ada@gmail.com', None, None],[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None],[3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None],[4, 'Art', 'Garfunkel', 'art@gmail.com', None, None],[1000, 'Jared', 'Hodgins', 'jh@gmail.com', 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86', None]]
        data = dict(firstname = 'Jared', lastname = 'Hodgins', contact = 'jh@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = post_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(True,result)
        self.assertEqual(actual,expected)
    #add user fail if already exist
    def test_add_user_fail(self):
        expected = [[1, 'Ada', 'Lovelace', 'ada@gmail.com', None, None],[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None],[3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None],[4, 'Art', 'Garfunkel', 'art@gmail.com', None, None]]
        data = dict(firstname = 'Ada', lastname = 'Lovelace', contact = 'ada@gmail.com', password = 'arrow')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = post_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(False,result)
        self.assertEqual(actual,expected)

    #testing user login
    def test_user_login(self):
        data = dict(firstname = 'Jared', lastname = 'Hodgins', contact = 'jh@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        post_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        print('added user to login')
        session = get_rest_call(self,'http://localhost:5000/users/login?firstname=Jared&pas=password')
        print("SESSION KEY " + session)
        self.assertNotEqual(session,"")


    #remove  user needing session key
    def test_delete_user(self):
        expected = [[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None],[3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None],[4, 'Art', 'Garfunkel', 'art@gmail.com', None, None]]
        data = dict(id = 1, firstname = 'Ada', lastname = 'Lovelace', contact = 'ada@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        put_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        print('updating ada to have password')

        session = get_rest_call(self,'http://localhost:5000/users/login?firstname=Ada&pas=password')
        print('session key aquired')

        result = delete_rest_call(self,'http://localhost:5000/users?firstname=Ada&lastname=Lovelace',{'session':session})
        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(actual,expected)
        self.assertEqual(True,result)
        
    #delete user fails as users doesnt exist
    def test_delete_user_fail(self):
        expected = [[1, 'Ada', 'Lovelace', 'ada@gmail.com', None, None],[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None],[3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None],[4, 'Art', 'Garfunkel', 'art@gmail.com', None, None]]
        result = delete_rest_call(self,'http://localhost:5000/users?firstname=Joe&lastname=Bobjoe')
        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(False,result)
        self.assertEqual(actual,expected)

    #delete user fails cause session key doesnt match user that is being deleted
    def test_delete_wrong_session(self):
        expected = [[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None], [3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None], [4, 'Art', 'Garfunkel', 'art@gmail.com', None, None], [1, 'Ada', 'Lovelace', 'ada@gmail.com', 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86', 'unkown']]
        data = dict(id = 1, firstname = 'Ada', lastname = 'Lovelace', contact = 'ada@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        put_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        print('updating ada to have password')

        session = get_rest_call(self,'http://localhost:5000/users/login?firstname=Ada&pas=password')
        print('session key aquired')
        print('Attempting to delete Jackie while logged in as Ada')
        result = delete_rest_call(self,'http://localhost:5000/users?firstname=Jackie&lastname=Gleason',{'session':session})
        actual = get_rest_call(self, 'http://localhost:5000/users')
        print(actual)
        #testing length as session key will be different every time
        self.assertEqual(len(actual),len(expected))
        self.assertEqual(False,result)

    #updating a user
    def test_update_user(self):
        expected = [[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None],[3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None],[4, 'Art', 'Garfunkel', 'art@gmail.com', None, None],[1, 'Ada', 'Shelley', 'ada@gmail.com', 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86', None]]
        data = dict(id = 1, firstname = 'Ada', lastname = 'Shelley', contact = 'ada@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = put_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(True,result)
        self.assertEqual(actual,expected)

    #updating a user fails as ID doesnt match
    def test_update_user_fail(self):
        expected = [[1, 'Ada', 'Lovelace', 'ada@gmail.com', None, None],[2, 'Mary', 'Shelley', 'mary@gmail.com', None, None],[3, 'Jackie', 'Gleason', 'jackie@gmail.com', None, None],[4, 'Art', 'Garfunkel', 'art@gmail.com', None, None]]
        data = dict(id = 10, firstname = 'Ada', lastname = 'Shelley', contact = 'ada@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = put_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(False,result)
        self.assertEqual(actual,expected)

    #getting all current checkouts
    def test_get_all_checkouts(self):
        expected = [[1, 1, 4, False], [2, 1, 3, False], [3, 2, 1, False], [4, 3, 1, False], [5, 2, 3, False]]
        actual = get_rest_call(self,'http://localhost:5000/checkout')
        self.assertEqual(actual,expected)

    #checking out works
    def test_checkout(self):
        expected = [[1, 1, 4, False], [2, 1, 3, False], [3, 2, 1, False], [4, 3, 1, False], [5, 2, 3, False], [1000, 1, 1, False]]
        data = dict(id = 1, firstname = 'Ada', lastname = 'Lovelace', contact = 'ada@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        put_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        print('updating ada to have password')

        session = get_rest_call(self,'http://localhost:5000/users/login?firstname=Ada&pas=password')
        print('session key aquired')

        data = dict(title = "Hobbit", reserve = False)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json', 'session': session}
        result = post_rest_call(self,'http://localhost:5000/checkout',jdata,hdr)
        actual = get_rest_call(self,'http://localhost:5000/checkout')
        print(actual)
        self.assertEqual(True,result)
        self.assertEqual(expected,actual)
    #checkout fails as no session
    def test_checkout_noSession(self):
        expected = [[1, 1, 4, False], [2, 1, 3, False], [3, 2, 1, False], [4, 3, 1, False], [5, 2, 3, False]]
        data = dict(title = "Hobbit", reserve = False)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json', 'session': 'asldkfja'}
        result = post_rest_call(self,'http://localhost:5000/checkout',jdata,hdr)
        actual = get_rest_call(self,'http://localhost:5000/checkout')
        self.assertEqual(False,result)
        self.assertEqual(expected,actual)
    
    #reserving works
    def test_checkout_reserve(self):
        expected = [[1, 1, 4, False], [2, 1, 3, False], [3, 2, 1, False], [4, 3, 1, False], [5, 2, 3, False], [1000, 1, 1, True]]
        data = dict(id = 1, firstname = 'Ada', lastname = 'Lovelace', contact = 'ada@gmail.com', password = 'password')
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        put_rest_call(self,'http://localhost:5000/users',jdata,hdr)
        print('updating ada to have password')

        session = get_rest_call(self,'http://localhost:5000/users/login?firstname=Ada&pas=password')
        print('session key aquired')

        data = dict(title = "Hobbit", reserve = True)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json', 'session': session}
        result = post_rest_call(self,'http://localhost:5000/checkout',jdata,hdr)
        actual = get_rest_call(self,'http://localhost:5000/checkout')
        self.assertEqual(True,result)
        self.assertEqual(expected,actual)