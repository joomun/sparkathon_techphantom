from . import db

class TeamPlan(db.Model):
    __tablename__ = 'team_plans'
    ID = db.Column(db.Integer, primary_key=True)  # It's good practice to have an ID as a primary key
    Row_Labels = db.Column(db.String(100), nullable=False)
    Count_of_EMPID = db.Column(db.Integer, nullable=False)
