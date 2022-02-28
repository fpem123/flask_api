import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from person.domain.personDomain import Person
from death.domain.deathDomain import Death

db = flask_sqlalchemy.SQLAlchemy()

def person_count():
    query = db.session.query(Person.person_id).count()
    
    return query

def person_gender_count():
    query = db.session.query(Person.gender_concept_id, 
        func.count(Person.gender_concept_id).label("count"))\
            .group_by(Person.gender_concept_id).all()

    return dict(query)

def person_race_count():
    query = db.session.query(Person.race_concept_id, 
        func.count(Person.race_concept_id).label("count"))\
            .group_by(Person.race_concept_id).all()

    return dict(query)

def person_ethnicity_count():
    query = db.session.query(Person.ethnicity_concept_id, 
        func.count(Person.ethnicity_concept_id).label("count"))\
            .group_by(Person.ethnicity_concept_id).all()

    return dict(query)

def person_death_count():
    query = db.session.query(Death.person_id).count()

    return query