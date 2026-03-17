from flask import Flask
from .extensions import db
from .config import Config   

from flask_migrate import Migrate  
from yardops.models import *  

migrate = Migrate()  


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)   


    @app.route("/")
    def home():
        return "YardOps Backend Running"

    return app