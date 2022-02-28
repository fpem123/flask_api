import flask_sqlalchemy
from sqlalchemy import ForeignKey

db = flask_sqlalchemy.SQLAlchemy()

class Visit(db.Model):
    __tablename__ = 'visit_occurrence'
    visit_occurrence_id = db.Column(db.Integer, primary_key=True)
    visit_concept_id = db.Column(db.Integer, db.ForeignKey("concept.concept.concept_id"))
    visit_start_datetime = db.Column(db.Date, nullable=False)
    visit_end_datetime  = db.Column(db.Date, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person.person_id"))
