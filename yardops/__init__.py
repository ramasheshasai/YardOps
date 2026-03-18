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

# ✅ Import models (required for migrations)
from yardops.models import Site, YardSpot, Trailer, Appointment

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(sites_bp)

    # Error handlers
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

    # Health check route
    @app.route("/")
    def home():
        return "YardOps Backend Running"

    return app