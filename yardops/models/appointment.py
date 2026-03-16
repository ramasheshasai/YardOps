from yardops.extensions import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer )
    trailer_id = db.Column(db.Integer,db.ForeignKey("trailers.id"),nullable=False)
    site_id = db.Column(db.Integer,db.ForeignKey("sites.id"),nullable=False)
    yard_spot_id = db.Column(db.Integer,db.ForeignKey("yard_spots.id"),nullable=False)
    gate_pass = db.Column(db.String(100))
    checked_in_at = db.Column(db.DateTime)
    checked_out_at = db.Column(db.DateTime)
    status = db.Column(db.String(20))