from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    db.init_app(app)
    migrate = Migrate(app, db)

    from routes import reg_routes
    reg_routes(app, db)

    return app
