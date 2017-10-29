from settings import db

class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True)
    password = db.Column(db.LargeBinary)