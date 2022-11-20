from views.map_page import views


def install(app):
    app.add_url_rule(
      '/map',
      view_func=views.MapView.as_view('map-page')
    )
