from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS
from flask_migrate import Migrate
from backend.encrypt import bcrypt
import os

from backend.database import db
from backend.routes import my_blueprint


def create_app(config="backend.config.Config"):
    app = Flask(
        __name__,
        static_folder="../frontend/static/",
        template_folder="../frontend/templates",
    )
    CORS(app, origins="*")

    app.config.from_object(config)

    db.init_app(app)
    migrate = Migrate(app, db)

    bcrypt.init_app(app)
    app.register_blueprint(my_blueprint, url_prefix="/")

    admin = Admin(app, name="Admin", template_mode="bootstrap3")
    from backend.models import User

    admin.add_view(ModelView(User, db.session))

    return app
