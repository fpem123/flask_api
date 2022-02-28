import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Concept(db.Model):
    __tablename__ = 'concept'
    concept_id = db.Column(db.Integer, primary_key=True)
    concept_name = db.Column(db.String(200), nullable=False)
    domain_id = db.Column(db.String(100), nullable=False)
