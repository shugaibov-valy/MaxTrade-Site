from flask import Flask
from views.views_routers import *

def make_app() -> Flask:


    # Initialization the app application
    app = Flask(__name__)
    auth_router.install(app)
    map_router.install(app)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    return app