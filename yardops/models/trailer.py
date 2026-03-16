from yardsops.extensions import db

class Trailder(db.Model):
    __tablename__ = 'trailers'

    id = db.Column(db..Integer,primary_key=True)
    trailer_number = db.Column(db.String(50), nullable=False)
    carrier_name = db.Column(db.String(255))
    trailer_type = db.Column(db.String(20))
    temp_setting = db.Column(db.Float,nullable=True)
