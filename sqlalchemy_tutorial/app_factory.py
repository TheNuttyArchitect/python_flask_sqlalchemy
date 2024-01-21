import os

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = g.db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=os.path.join('sqlite:///mydb.db'),
    )

    if test_config is None:
        app.config.from_file('config.py', load=0, silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/healthcheck', methods=('GET',))
    def healthcheck():
        return "alive"
    
    # db = SQLAlchemy(app)
    # Migrate(app, db)
    # db.init_app(app)
    from .db_factory import init_db
    with app.app_context():
        init_db(app)
        #g.db = db

   #  from . import db_factory
   # with app.app_context():
   #     db_factory.init_app()
    
    return app
