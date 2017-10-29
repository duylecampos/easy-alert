import bcrypt

from models import Auth

def authenticate(username, password):
    user = Auth.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
        return user

def identity(payload):
    user_id = payload['identity']
    return Auth.query.filter_by(id=user_id).first()