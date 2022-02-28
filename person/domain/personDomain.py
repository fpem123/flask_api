import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    gender_concept_id = db.Column(db.Integer, db.ForeignKey("concept.concept.concept_id"))
    birth_datetime = db.Column(db.Date, nullable=False)
    race_concept_id = db.Column(db.Integer, db.ForeignKey("concept.concept.concept_id"))
    ethnicity_concept_id = db.Column(db.Integer, db.ForeignKey("concept.concept.concept_id"))
