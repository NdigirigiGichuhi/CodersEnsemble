from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()

def create_app():
    app.config.from_object("config.Config")
    db.init_app(app)
    migrate.init_app(db)
    login_manager.init_app(app)

    from my_app.views.auth import auth_bp

    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app