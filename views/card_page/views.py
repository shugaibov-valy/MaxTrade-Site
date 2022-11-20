from flask import redirect, render_template, request, session
from flask.views import MethodView
from api import get_complaint_by_id, get_user_by_id


class CardView(MethodView):
    def get(self, complaint_id):
        print(complaint_id)
        info = get_complaint_by_id(complaint_id)
        author = get_user_by_id(info['authorId'])
        return render_template('card.html', info=info, author=author)

    def post(self):
        pass
