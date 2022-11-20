
from views.ai_page import views


def install(app):
    app.add_url_rule(
      '/ai',
      view_func=views.AIView.as_view('ai-page')
    )


