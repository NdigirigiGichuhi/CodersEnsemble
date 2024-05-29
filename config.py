import os

# Database configuration
DB_NAME = "database.db"
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Configuration class for the application.
    Attributes:
        SECRET_KEY (str): A secret key for the application,
        used for session management and other security-related tasks.
        SQLALCHEMY_DATABASE_URI (str): The database URI that should
                        be used for the connection.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): A flag to disable
                        or enable modification tracking in SQLAlchemy.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
            'd329419510d8a8f0d6135315dfce2cfea69e434acTY'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
