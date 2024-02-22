from flask_restx import Resource


class APIResource(Resource):
    def __init__(self, api):
        Resource.__init__(self, api)
