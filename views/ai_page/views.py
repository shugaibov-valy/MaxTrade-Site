from flask import redirect, render_template, request, session
from flask.views import MethodView
from api import auth_user, get_complaints, get_marks
from geocoder import address_to_coords, coords_to_address
from folium_api import generate_map
from get_predict import predict_text
import os


class AIView(MethodView):
    def get(self):
        return render_template("ai.html")

    def post(self):
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join("./upload", file1.filename)
        file1.save(path)
        return predict_text(path)

