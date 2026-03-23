from flask import Flask, jsonify
from flask_migrate import Migrate
from .extensions import db 
from config import Config 

from yardops.errors import ( 
    TrailerNotFoundError,
    TrailerAlreadyCheckedInError,
    NoAvailableSpotError,
    SpotOccupiedError
)
from yardops.blueprints.sites import sites_bp
from yardops.blueprints.dashboard import dashboard_bp
from yardops import models
migrate = Migrate()
from yardops.blueprints.trailers import trailers_bp
from yardops.factories.appointment_factory import AppointmentFactory
from yardops.blueprints.appointments import appointments_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(sites_bp)
    app.register_blueprint(trailers_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(dashboard_bp)

    @app.errorhandler(TrailerNotFoundError)
    def handle_trailer_not_found(error):
        return jsonify({"error": error.message}), 404

    @app.errorhandler(TrailerAlreadyCheckedInError)
    def handle_already_checked_in(error):
        return jsonify({"error": error.message}), 400

    @app.errorhandler(NoAvailableSpotError)
    def handle_no_spot(error):
        return jsonify({"error": error.message}), 400

    @app.errorhandler(SpotOccupiedError)
    def handle_spot_occupied(error):
        return jsonify({"error": error.message}), 400

    @app.route("/")
    def home():
        return "YardOps Backend Running"

    return app