
from flask_restful import Resource
import logging as logger

class Task(Resource):


    def get(self):
        logger.debug("inside get")
        return {"message": "inside get method"},200
    def post(self):
        logger.debug("inside post")
        return {"message": "inside post method"},200

    def put(self):
        logger.debug("inside put")
        return {"message": "inside put method"},200

    def delete(self):
        logger.debug("inside delete")
        return {"message": " inside delete method"},200
