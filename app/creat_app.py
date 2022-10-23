from flask import Flask
from app.main.views import main_blueprint
from app.post.views import post_blueprint

def create_app():

    app = Flask(__name__)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(post_blueprint)

    return app