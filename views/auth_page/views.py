from flask import redirect, render_template, request, session
from flask.views import MethodView
from api import auth_user, get_complaints, get_marks
from geocoder import address_to_coords, coords_to_address
from folium_api import generate_map



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


class SearchAddressView(MethodView):
    def get(self):
        pass

    def post(self, address):
        find_coords = address_to_coords(address).split(" ")
        address = coords_to_address(find_coords[0], find_coords[1])
        marks = get_marks()
        complaints = get_complaints()
        generate_map(default_address=address, default_location=find_coords, complaints=complaints, marks=marks)
        return '1'
