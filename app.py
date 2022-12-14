from flask import Flask
from views.views_routers import *

def make_app() -> Flask:


    # Initialization the app application
    app = Flask(__name__)

    UPLOAD_FOLDER = './upload'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    auth_router.install(app)
    map_router.install(app)
    card_router.install(app)
    mark_router.install(app)

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    return app

