import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Condition(db.Model):
    __tablename__ = 'condition_occurrence'
    condition_occurrence_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person.person_id"))
    condition_concept_id = db.Column(db.Integer, db.ForeignKey("concept.concept.concept_id"))
    condition_start_datetime = db.Column(db.Date, nullable=False)
    condition_end_datetime = db.Column(db.Date, nullable=False)
    visit_occurrence_id = db.Column(db.Integer, db.ForeignKey("visit_occurrence.visit_occurrence.concept.concept_id"))
