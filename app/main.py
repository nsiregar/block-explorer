from app import app
from controllers import home_view

app.register_blueprint(home_view)