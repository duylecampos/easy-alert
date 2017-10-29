from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

import models
from settings import db
from utils import authenticate

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)

class Auth(Resource):

    def post(self):
        args = parser.parse_args()
        user = authenticate(args['username'], args['password'])
        if user:
            return {'access_token': create_access_token({'identity': user.username, 'type': 'user'})}
        return {"msg": "Bad username or password"}, 401