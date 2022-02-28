import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from visit.domain.visitDomain import Visit
from person.domain.personDomain import Person

db = flask_sqlalchemy.SQLAlchemy()

def visit_concept_count():
    query = db.session.query(Visit.visit_concept_id, 
        func.count(Visit.visit_concept_id).label("count")).group_by(Visit.visit_concept_id).all()
    
    return dict(query)

def visit_gender_count():
    query = db.session.query(Person.gender_concept_id, 
        func.count(Person.gender_concept_id).label("count")).join(Visit, Person.person_id==Visit.person_id)\
            .group_by(Person.gender_concept_id).all()

    return dict(query)

def visit_race_count():
    query = db.session.query(Person.race_concept_id, 
        func.count(Person.race_concept_id).label("count")).join(Visit, Person.person_id==Visit.person_id)\
            .group_by(Person.race_concept_id).all()

    return dict(query)

def visit_ethnicity_count():
    query = db.session.query(Person.ethnicity_concept_id, 
        func.count(Person.ethnicity_concept_id).label("count")).join(Visit, Person.person_id==Visit.person_id)\
            .group_by(Person.ethnicity_concept_id).all()

    return dict(query)