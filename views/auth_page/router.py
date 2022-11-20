
from views.auth_page import views


def install(app):
    app.add_url_rule(
      '/',
      view_func=views.LoginView.as_view('auth-page')
    )

    app.add_url_rule(
      '/get_map/address=<string:address>',
      view_func=views.SearchAddressView.as_view('get_map-page')
    )
