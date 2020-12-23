from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from cardgame.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from cardgame.users.routes import users
    from cardgame.main.routes import main
    from cardgame.game.routes import game
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(game)

    return app


def setup_db():
    app = create_app()
    app.app_context().push()
    db.drop_all()
    db.create_all()
