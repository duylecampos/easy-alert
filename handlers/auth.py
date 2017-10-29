import bcrypt

from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

import models
from settings import db

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)

class Auth(Resource):

    def post(self):
        args = parser.parse_args()
        user = models.Auth.query.filter_by(username=args['username']).first()
        if user and bcrypt.checkpw(args['password'].encode('utf-8'), user.password):
            return {'access_token': create_access_token({'identity': user.username, 'type': 'user'})}
        return {"msg": "Bad username or password"}, 401