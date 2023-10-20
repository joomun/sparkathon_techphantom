from . import db

class Employee(db.Model):
    __tablename__ = 'employees'
    EMPID = db.Column(db.Integer, primary_key=True)
    TeamID = db.Column(db.Integer, nullable=False)
    EMPNAME = db.Column(db.String(100), nullable=False)
    AD1 = db.Column(db.String(100))
    AD2 = db.Column(db.String(100))
    AD3 = db.Column(db.String(100))
