import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Death(db.Model):
    __tablename__ = 'death'
    
    person_id = db.Column(db.Integer, primary_key=True)
    death_date = db.Column(db.Date)
