from flask import Blueprint, jsonify
from yardops.extensions import redis_client
from yardops.models.appointment import Appointment
from yardops.models.site import Site

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/api/dashboard")
@dashboard_bp.route("/<int:site_id>", methods=["GET"])
def get_count(site_id):
    key = f"yard:{site_id}:trailer_count"

    
    count = redis_client.get(key)

    if count:
        count = int(count.decode("utf-8"))

    else:    
        count = Appointment.query.filter_by(
            site_id=site_id,
            status="CHECKED_IN"
        ).count()

       
        redis_client.set(key, count)

    return jsonify({
        "site_id": site_id,
        "trailer_count": count
    }), 200

@dashboard_bp.route("/warm", methods=["POST"])
def warmer():
    sites = Site.query.all()

    result = []

    for site in sites:
        count = Appointment.query.filter_by(
            site_id=site.id,
            status="CHECKED_IN"
        ).count()

        key = f"yard:{site.id}:trailer_count"

        redis_client.set(key, count)

        result.append({
            "site_id": site.id,
            "trailer_count": count
        })

    return jsonify({
        "message": "Cache warmed successfully",
        "data": result
    }), 200
