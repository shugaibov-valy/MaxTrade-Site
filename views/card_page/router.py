from views.card_page import views


def install(app):
    app.add_url_rule(
      '/card/<int:complaint_id>',
      view_func=views.CardView.as_view('card-page')
    )
