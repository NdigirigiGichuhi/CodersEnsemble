from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bcrypt import Bcrypt 


# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()



def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask app instance.
    """
    app = Flask(__name__)
    bcrypt = Bcrypt()

    # Load the configuration from the config module
    app.config.from_object(Config)

    # Initialize Flask extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Register Blueprints
    from app.views.auth import auth_bp
    from app.views.main import main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
