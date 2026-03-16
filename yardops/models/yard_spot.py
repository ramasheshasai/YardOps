from yarndops.extensions import db

class YardSopt(db.Model):
    __tablename__ = 'yard_spots'
    
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer,db.ForeignKey("sites.id"),nullable=False)
    spot_label = db.Colunn(db.string(255),nullable=False)
    is_occupied = db.Column(db.Boolean, default=False)