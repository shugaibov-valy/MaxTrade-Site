from views.mark_page import views


def install(app):
    app.add_url_rule(
      '/mark/create_mark/latitude=<string:latitude>&longitude=<string:longitude>',
      view_func=views.CreateMarkView.as_view('mark_create-page')
    )
    
    app.add_url_rule(
      '/mark/<int:mark_id>',
      view_func=views.MarkView.as_view('mark-page')
    )