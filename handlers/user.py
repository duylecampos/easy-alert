import bcrypt

from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt_identity

import models
from settings import db

from utils import login_required

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

    @login_required
    def get(self):
        current_identity = get_jwt_identity()
        return {'logged_user': current_identity['identity']}