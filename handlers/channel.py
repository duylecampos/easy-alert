import bcrypt

from flask import request, jsonify
from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import get_jwt_identity, create_access_token
from sqlalchemy.exc import IntegrityError

import models
from settings import db
from utils import login_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)

class Channels(Resource):

    @login_required
    def post(self):
        args = parser.parse_args()
        try:
            channel = models.Channel(name=args['name'])
            db.session.add(channel)
            db.session.commit()
        except IntegrityError:
            return 'Unavailable channel name!', 400
        return {
            'name': channel.name,
            'slug': channel.slug,
            'token': create_access_token({'identity': channel.slug, 'type': 'channel'})
        }, 201


class Channel(Resource):

    @login_required
    def get(self, channel_slug):
        channel = models.Channel.query.filter_by(slug=channel_slug).first()
        if not channel:
            abort(404, message="Channel {} doesn't exist".format(channel_slug))
        return {
            'name': channel.name,
            'slug': channel.slug,
            'token': create_access_token({'identity': channel.slug, 'type': 'channel'})
        }, 200