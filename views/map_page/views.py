from flask import redirect, render_template, request, session
from flask.views import MethodView
from folium_api import generate_map
from api import get_complaints

class MapView(MethodView):
    def get(self):
        data = get_complaints()
        generate_map(data)
        return render_template("map.html")

    def post(self):
        pass
