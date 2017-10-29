import bcrypt

from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

import models
from settings import db

class User(Resource):

    def post(self):
        args = request.get_json()
        username = args['username']
        password = bcrypt.hashpw(args['password'].encode('utf-8'), bcrypt.gensalt())
        try:
            user = models.Auth(username=username, password=password)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return 'Unavailable username!', 400
        return '', 201

    @jwt_required()
    def get(self):
        return {'logged_user': current_identity.username}