import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Drug(db.Model):
    __tablename__ = 'drug_exposure'
    drug_exposure_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person.person_id"))
    drug_concept_id = db.Column(db.Integer, db.ForeignKey("concept.concept.concept_id"))
    drug_exposure_start_datetime = db.Column(db.Date, nullable=False)
    drug_exposure_end_datetime = db.Column(db.Date, nullable=False)
    visit_occurrence_id = db.Column(db.Integer, db.ForeignKey("visit_occurrence.visit_occurrence.concept.concept_id"))