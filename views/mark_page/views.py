from flask import redirect, render_template, request, session
from flask.views import MethodView
from folium_api import generate_map
from api import create_mark, get_mark_by_id, update_mark


class CreateMarkView(MethodView):
    def get(self, latitude, longitude):
        return render_template("create_mark.html")

    def post(self, latitude, longitude):
        desc = request.form.get('description')
        mark = create_mark(longitude, latitude, desc)
        return redirect("/map")


class MarkView(MethodView):
    def get(self, mark_id):
        mark = get_mark_by_id(mark_id)
        return render_template("mark_card.html", info=mark)

    def post(self, mark_id):
        desc = request.form.get('description')
        update_mark(mark_id, desc)
        return redirect("/map")