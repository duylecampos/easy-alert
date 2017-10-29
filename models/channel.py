import uuid
import bcrypt
import jwt

from settings import db
from utils import slugify

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    slug = db.Column(db.String(50))
    active =  db.Column(db.Boolean, default=True)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super().__init__(*args, **kwargs)