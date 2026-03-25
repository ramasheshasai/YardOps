from flask import Blueprint, jsonify, request
from yardops.extensions idbmport 
from yardops.models.trailer import Trailer
from yardops.factories.trailer_factory import TrailerFactory

trailers_bp = Blueprint("trailers", __name__, url_prefix="/api/trailers")


@trailers_bp.route("", methods=["POST"])
def create_trailer():
    data = request.get_json()

    try:
        trailer =TrailerFactory.create(
            trailer_type=data.get("trailer_type"),
            trailer_number=data.get("trailer_number"),
            carrier_name=data.get("carrier_name"),
            temp_setting=data.get("temp_setting")
        )   

        db.session.add(trailer)
        db.session.commit()

        return jsonify({
            "id": trailer.id,
            "trailer_type": trailer.trailer_type,
            "trailer_number": trailer.trailer_number,
            "carrier_name": trailer.carrier_name,
            "temp_setting": trailer.temp_setting
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@trailers_bp.route("", methods=["GET"])
def get_trailers():
    trailer_type = request.args.get("trailer_type")
    carrier_name = request.args.get("carrier_name")

    query = Trailer.query

    if trailer_type:
        query = query.filter_by(trailer_type=trailer_type.upper())

    if carrier_name:
        query = query.filter_by(carrier_name=carrier_name)

    trailers = query.all()

    result = []
    for trailer in trailers:
        result.append({
            "id": trailer.id,
            "trailer_type": trailer.trailer_type,
            "trailer_number": trailer.trailer_number,
            "carrier_name": trailer.carrier_name,
            "temp_setting": trailer.temp_setting
        })

    return jsonify(result), 200