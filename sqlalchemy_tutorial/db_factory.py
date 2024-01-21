from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from werkzeug.local import LocalProxy

import click
from flask import current_app, g

def init_db(app):
    db = SQLAlchemy(app)
    Migrate(app, db)

    g.db = db

def get_db():
    # if 'db' not in g:
    #    db = SQLAlchemy()
    #    db.init_app()
    #    g.db = db


    return g.db


# def init_db():
    # if not database_exists(current_app.config['SQLALCHEMY_DATABASE_URI']):
    #    create_database(current_app.config['SQLALCHEMY_DATABASE_URI'])
    #with app.app_context():
    # db = LocalProxy(get_db)
#    db = get_db()
#    Migrate(current_app, db)
        
    
# @click.command('init-db')
# def init_db_command():
#    init_db()


# def init_app():
#    init_db()
    # app.teardown_appcontext()
    # app.cli.add_command(init_db_command)
