from flask import redirect, render_template, request, session
from flask.views import MethodView
from folium_api import generate_map
from api import get_complaints, get_marks

class MapView(MethodView):
    def get(self):
        complaints = get_complaints()
        marks = get_marks()
        generate_map(complaints=complaints, marks=marks)
        return render_template("map.html")

    def post(self):
        pass
