from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail
from flask_cors import CORS
from flask_migrate import Migrate
import os

from backend.database import db
from backend.routes import my_blueprint

mail = Mail()

def create_app():
    app = Flask(__name__, static_folder='../frontend/static/', template_folder='../frontend/templates')
    app.secret_key = os.urandom(24)
    CORS(app, origins='*')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///durgapuja.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Flask-Mail configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'sonarcityrpujo@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Abcd!234'
    app.config['MAIL_DEFAULT_SENDER'] = 'sonarcityrpujo@gmail.com'

    db.init_app(app)
    mail.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    app.register_blueprint(my_blueprint, url_prefix='/')

    # Initialize Flask-Admin
    admin = Admin(app, name='Admin', template_mode='bootstrap3')

    # Import the User model here to avoid circular import issues
    from backend.models import User

    # Add the User model to the admin interface
    admin.add_view(ModelView(User, db.session))

    return app

def get_image_files(folder_path):

    image_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpeg', '.png', '.gif')):
            image_files.append(filename)
    return image_files
