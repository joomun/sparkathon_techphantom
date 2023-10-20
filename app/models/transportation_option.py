from . import db

class TransportationOption(db.Model):
    __tablename__ = 'transportation_options'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Seating_Capacity = db.Column(db.Integer, nullable=False)
    Cost_per_kilometer_in_Rs = db.Column(db.Float, nullable=False)
