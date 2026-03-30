from flask import Blueprint, request, jsonify
from yardops.extensions import db
from yardops.models.appointment import Appointment
from yardops.factories.appointment_factory import AppointmentFactory
from yardops.models.yard_spot import YardSpot
from yardops.extensions import redis_client

appointments_bp = Blueprint("appointments",__name__,url_prefix="/appointments")

@appointments_bp.route("/checkin", methods=["POST"])
def checkin():
    data = request.get_json()

    site_id = data.get("site_id")
    trailer_id = data.get("trailer_id")
    preferred_spot_id = data.get("preferred_spot_id")

    if not trailer_id or not site_id:
          return jsonify({"error": "missing required fields"}), 400
    
    try:
        appointment = AppointmentFactory.create_checkin(
            site_id=site_id,
            trailer_id=trailer_id,
            preferred_spot_id=preferred_spot_id
        )
        redis_client.incr(f"yard:{site_id}:trailer_count")

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

    return jsonify({
        "id": appointment.id,
        "status": appointment.status,
        "gate_pass": appointment.gate_pass,
        "yard_spot_id": appointment.yard_spot_id
    }), 201

@appointments_bp.route("/<int:appointment_id>/checkout", methods=["POST"])
def checkout(appointment_id):
    appointment = Appointment.query.get(appointment_id)

    if not appointment:
        return jsonify({"error": "appointment not found"}), 404

    spot = YardSpot.query.get(appointment.yard_spot_id)

    appointment.status = "CHECKED_OUT"
    if spot:
        spot.is_occupied = False

    db.session.commit()

    redis_client.decr(f"yard:{appointment.site_id}:trailer_count")

    return jsonify({
        "message": "checked out successfully",
        "appointment_id": appointment.id
    })
