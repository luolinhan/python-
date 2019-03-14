# coding=utf-8
import sys
from flask import Flask
import flask_restful


app = Flask(__name__)
api = flask_restful.Api(app)

class example(flask_restful.Resource):
    def get(self):
        return {'班级': '初一1班'}

api.add_resource(example, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
