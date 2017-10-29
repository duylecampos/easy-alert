from handlers import User

def load(api):
    api.add_resource(User, '/user')