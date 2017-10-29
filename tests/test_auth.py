import bcrypt
import unittest

from flask_testing import TestCase

from settings import db
from app import create_app
from authentication import authenticate
import models


class TestAuth(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self.SQLALCHEMY_DATABASE_URI)

    def setUp(self):
        db.create_all()
        password = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt(4)) # For testing the round number was changed
        self.created_user = models.Auth(username='username', password=password)
        db.session.add(self.created_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_creation(self):
        selected_user = models.Auth.query.filter_by(username='username').first()
        assert self.created_user == selected_user

    def test_user_login(self):
        logged_user = authenticate('username', 'password')
        assert logged_user == self.created_user
