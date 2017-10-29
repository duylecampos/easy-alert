import unittest

from flask_testing import TestCase

from settings import db
from app import create_app
import models


class TestAuth(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        return create_app(self.SQLALCHEMY_DATABASE_URI)

    def setUp(self):
        db.create_all()

        self.created_channel = models.Channel(
            name='Channel 1'
        )
        db.session.add(self.created_channel)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_channel_creation(self):
        selected_channel = models.Channel.query.filter_by(slug='channel-1').first()
        assert self.created_channel == selected_channel

    def test_channel_select(self):
        pass

    
