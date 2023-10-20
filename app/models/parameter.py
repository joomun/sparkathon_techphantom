from . import db

class Parameter(db.Model):
    __tablename__ = 'parameters'
    ID = db.Column(db.Integer, primary_key=True)  # It's good practice to have an ID as a primary key
    Challenge = db.Column(db.String(100), nullable=False)
    Parameter = db.Column(db.String(100), nullable=False)
    Value = db.Column(db.String(100), nullable=False)
