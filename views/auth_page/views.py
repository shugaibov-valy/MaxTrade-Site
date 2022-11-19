from flask import redirect, render_template, request, session
from flask.views import MethodView
from api import auth_user

class LoginView(MethodView):
    def get(self):
        return render_template("auth.html")

    def post(self):
        login_form = request.form.get('login')
        password_form = request.form.get('password')
        result = auth_user(login_form, password_form)
        if result['result'] == 'success' and result['is_admin'] == True:
            return redirect('/map')
        return render_template("auth.html", error_message="Неверный логин или пароль!")
