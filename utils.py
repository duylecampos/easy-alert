import re
import bcrypt
import uuid
from unicodedata import normalize
from functools import wraps

from flask_jwt_extended import get_jwt_identity, jwt_required

from models import Auth

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word.decode("utf-8"))
    return delim.join(result)

def login_required(f):
    @jwt_required
    @wraps(f)
    def decorated_function(*args, **kwargs):
        identity = get_jwt_identity()
        return f(*args, **kwargs)
    return decorated_function

def authenticate(username, password): 
    user = Auth.query.filter_by(username=username).first() 
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password): 
        return user
    return None