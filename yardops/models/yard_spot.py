from yardops.extensions import db

class YardSpot(db.Model):
    __tablename__ = 'yard_spots'
    
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer,db.ForeignKey("sites.id"),nullable=False)
    spot_label = db.Column(db.String(255),nullable=False)
    is_occupied = db.Column(db.Boolean, default=False)

    site = db.relationship("Site", back_populates="yard_spots")
    appointments = db.relationship("Appointment", back_populates="yard_spot")