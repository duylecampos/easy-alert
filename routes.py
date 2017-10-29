from handlers import User, Channels, Channel, Auth

def load(api):
    api.add_resource(Auth, '/auth')
    api.add_resource(User, '/user')
    api.add_resource(Channels, '/channel')
    api.add_resource(Channel, '/channel/<channel_slug>')