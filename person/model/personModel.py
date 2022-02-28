import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import aliased
from person.domain.personDomain import Person
from death.domain.deathDomain import Death
from concept.domain.conceptDomain import Concept
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

def person_row_search(column, keyword, start, many):
    res = {}
    cnt = 0
    concept1 = aliased(Concept)
    concept2 = aliased(Concept)
    concept3 = aliased(Concept)

    if column =="person_id":
        keyword = int(keyword)
        query = db.session.query(Person.person_id, concept1.concept_name.label("gender_concept_name"),
                Person.birth_datetime, concept2.concept_name.label("race_concept_name"), 
                concept3.concept_name.label("ethnicity_concept_name"))\
                .join(concept1, Person.gender_concept_id==concept1.concept_id)\
                .join(concept2, Person.race_concept_id==concept2.concept_id)\
                .join(concept3, Person.ethnicity_concept_id==concept3.concept_id)\
                .filter(Death.person_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="birth_datetime":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Person.person_id, concept1.concept_name.label("gender_concept_name"),
                Person.birth_datetime, concept2.concept_name.label("race_concept_name"), 
                concept3.concept_name.label("ethnicity_concept_name"))\
                .join(concept1, Person.gender_concept_id==concept1.concept_id)\
                .join(concept2, Person.race_concept_id==concept2.concept_id)\
                .join(concept3, Person.ethnicity_concept_id==concept3.concept_id)\
                .filter(Person.birth_datetime == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="gender_concept_id":
        keyword = int(keyword)
        query = db.session.query(Person.person_id, concept1.concept_name.label("gender_concept_name"),
                Person.birth_datetime, concept2.concept_name.label("race_concept_name"), 
                concept3.concept_name.label("ethnicity_concept_name"))\
                .join(concept1, Person.gender_concept_id==concept1.concept_id)\
                .join(concept2, Person.race_concept_id==concept2.concept_id)\
                .join(concept3, Person.ethnicity_concept_id==concept3.concept_id)\
                .filter(Person.gender_concept_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="race_concept_id":
        keyword = int(keyword)
        query = db.session.query(Person.person_id, concept1.concept_name.label("gender_concept_name"),
                Person.birth_datetime, concept2.concept_name.label("race_concept_name"), 
                concept3.concept_name.label("ethnicity_concept_name"))\
                .join(concept1, Person.gender_concept_id==concept1.concept_id)\
                .join(concept2, Person.race_concept_id==concept2.concept_id)\
                .join(concept3, Person.ethnicity_concept_id==concept3.concept_id)\
                .filter(Person.race_concept_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="ethnicity_concept_id":
        keyword = int(keyword)
        query = db.session.query(Person.person_id, concept1.concept_name.label("gender_concept_name"),
                Person.birth_datetime, concept2.concept_name.label("race_concept_name"), 
                concept3.concept_name.label("ethnicity_concept_name"))\
                .join(concept1, Person.gender_concept_id==concept1.concept_id)\
                .join(concept2, Person.race_concept_id==concept2.concept_id)\
                .join(concept3, Person.ethnicity_concept_id==concept3.concept_id)\
                .filter(Person.ethnicity_concept_id == keyword)\
                .offset(start).limit(start+many).all()
    else:
        query = db.session.query(Person.person_id, concept1.concept_name.label("gender_concept_name"),
                Person.birth_datetime, concept2.concept_name.label("race_concept_name"), 
                concept3.concept_name.label("ethnicity_concept_name"))\
                .join(concept1, Person.gender_concept_id==concept1.concept_id)\
                .join(concept2, Person.race_concept_id==concept2.concept_id)\
                .join(concept3, Person.ethnicity_concept_id==concept3.concept_id)\
                .offset(start).limit(start+many).all()

    for row in query:
        res[cnt] = dict(row)
        cnt += 1

    return res

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