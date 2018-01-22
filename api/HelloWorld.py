from flask import Blueprint
from flask_restful import Resource, Api, abort, reqparse
from Logger import logger, LogLevel, TraceException
import logging
# from app import logger


API_VERSION_V1 = 1
API_VERSION = 1

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)

MESSAGES = {'1': 'Hello', '2': 'Thanks', '3': 'Goodbye', '4': 'Please'}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in MESSAGES:
        abort(404, message="message {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('content')


class HelloWorldList(Resource):
    def get(self):
        logger.log(LogLevel.DEBUG, 'log from HelloWorldList')
        try:
            return MESSAGES[100]
        except Exception as ex:
            logger.log(LogLevel.ERROR, TraceException(ex.__str__()).message)
        return MESSAGES

    def post(self):
        args = parser.parse_args()
        print(args)
        new_index = len(MESSAGES) + 1
        MESSAGES[str(new_index)] = args['content']
        return MESSAGES[str(new_index)], 201


class HelloWorld(Resource):
    def get(self, message):
        abort_if_todo_doesnt_exist(message)
        return MESSAGES[message]

    def delete(self, message):
        abort_if_todo_doesnt_exist(message)
        value = MESSAGES[message]
        del MESSAGES[message]
        return value, 204

    def put(self, message):
        args = parser.parse_args()
        print(args)
        content = args['content']
        MESSAGES[message] = content
        return message, 201


api_v1.add_resource(HelloWorldList, '/helloworld')
api_v1.add_resource(HelloWorld, '/helloworld/<message>')
