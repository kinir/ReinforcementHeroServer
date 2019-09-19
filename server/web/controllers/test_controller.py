from flask_restful import Resource

class Test(Resource):

    def get(self):
        a = 0
        for i in range(100000000):
            a += i

        return a