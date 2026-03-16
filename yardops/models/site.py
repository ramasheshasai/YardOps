from yarndrops.extensions import db

class Site(db.Model):
    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
