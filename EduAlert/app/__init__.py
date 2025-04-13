from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '515244da1516f77edbdf63470174f664'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edualert.db'
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
