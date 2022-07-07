import flask
from flask import Flask, request, url_for

from profilephoto import ProfilePhotoGetter

app = Flask(__name__, static_folder='user_photos')
profile_photo_getter = ProfilePhotoGetter()


@app.route("/")
def index():
    return "Hello World!"


@app.route('/get_profile_photo', methods=['GET'])
def get_profile_photo():
    args = request.args
    user_id = args['user_id']
    
    filename = profile_photo_getter.get(user_id)
    if filename:
        return f'{request.host_url}{filename}'
    else:
        return 'None'
