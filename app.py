import os

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

import routes
from settings import db
from authentication import authenticate, identity

def create_app(db_uri):
    # Load config file to environment var
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    api = Api(app)
    db.init_app(app)
    jwt = JWT(app, authenticate, identity)

    routes.load(api)

    return app

if __name__ == '__main__':
    app = create_app(os.environ.get('DB_URI'))
    app.run(debug=True)