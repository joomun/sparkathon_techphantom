from . import db

class PartyPlace(db.Model):
    __tablename__ = 'party_places'
    ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(100), nullable=False)
    Region = db.Column(db.String(100))
    AD1 = db.Column(db.String(100))
    AD2 = db.Column(db.String(100))
    AD3 = db.Column(db.String(100))
