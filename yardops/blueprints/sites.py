from flask import Blueprint, request, jsonify
from yardops.extensions import db
from yardops.models.site import Site
from yardops.models.yard_spot import YardSpot

sites_bp = Blueprint("sites", __name__, url_prefix="/api/sites")


@sites_bp.route("", methods=["POST"])
def create_site():
    data = request.get_json()

    site = Site(
        name=data.get("name"),
        address=data.get("address")
    )

    db.session.add(site)
    db.session.commit()

    return jsonify({
        "id": site.id,
        "name": site.name,
        "address": site.address
    }), 201


@sites_bp.route("/<int:site_id>", methods=["GET"])
def get_site(site_id):
    site = Site.query.get(site_id)

    if not site:
        return jsonify({"error": "Site not found"}), 404

    return jsonify({
        "id": site.id,
        "name": site.name,
        "address": site.address
    })

@sites_bp.route("/<int:site_id>/spots", methods=["POST"])
def create_spot(site_id):
    data = request.get_json()

    site = Site.query.get(site_id)

    if not site:
        return jsonify({"error": "Site not found"}), 404

    spot = YardSpot(
        site_id=site.id,
        spot_label=data.get("spot_label"),
        is_occupied=False
    )

    db.session.add(spot)
    db.session.commit()

    return jsonify({
        "id": spot.id,
        "spot_label": spot.spot_label,
        "site_id": spot.site_id
    }), 201