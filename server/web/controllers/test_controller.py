from flask import request
from flask_restful import Resource

class Test(Resource):

    def get(self, id):
        print(f"Server start with id: {id}")
        a = 0
        for i in range(100000000):
            #print(f"id: {id}")
            a += i
        
        print(f"Server done with id: {id}")
        return a