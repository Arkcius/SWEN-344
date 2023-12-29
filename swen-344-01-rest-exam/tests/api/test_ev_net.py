import unittest
import json
from tests.test_utils import *

class TestEV_Net(unittest.TestCase):

    #Small utility for printing a list of items; one per line
    def print_list(self, list):
        for item in list:
            print(item)

    def test_example_endpoint(self):
        actual = get_rest_call(self, 'http://localhost:5000/manufacturer')
        assert(len(actual) == 8)

    def test_search_endpoint(self):
        result = get_rest_call(self, 'http://localhost:5000/manufacturer/2')
        print(result)
        result = get_rest_call(self, 'http://localhost:5000/manufacturer/name/Ford')
        print(result)

    def test_01_inventory(self):
        actual = get_rest_call(self, 'http://localhost:5000/inventory')
        print()
        for item in actual:
            print(item)

    def test_02_add_new_vehicle(self):
        before = get_rest_call(self, 'http://localhost:5000/inventory')
        print()
        print("Before")
        for item in before:
            print(item)
        data = dict(manufacturer = 'BMW',type = 'PLUG-IN HYBRID',model = 'x45e',description = 'a bit big, but comfy!',quantity = 3)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        post_rest_call(self,'http://localhost:5000/inventory',jdata,hdr)
        after = get_rest_call(self, 'http://localhost:5000/inventory')
        print()
        print("After")
        for item in after:
            print(item)
