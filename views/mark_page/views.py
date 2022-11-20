from flask import redirect, render_template, request, session
from flask.views import MethodView
from folium_api import generate_map
from api import create_mark

class CreateMarkView(MethodView):
    def get(self, latitude, longitude):
        print(latitude, longitude)
        return render_template("create_mark.html")

    def post(self, latitude, longitude):
        desc = request.form.get('description')
        print(latitude, longitude)
        mark = create_mark(longitude, latitude, desc)
        return redirect("/map")