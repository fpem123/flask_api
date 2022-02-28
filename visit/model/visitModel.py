import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from visit.domain.visitDomain import Visit
from concept.domain.conceptDomain import Concept
from person.domain.personDomain import Person
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

def visit_row_search(column, keyword, start, many):
    res = {}
    cnt = 0

    if column =="visit_occurrence_id":
        keyword = int(keyword)
        query = db.session.query(Visit.visit_occurrence_id, Concept.concept_name.label("visit_occurrence_name"), 
                Visit.visit_start_datetime, Visit.visit_end_datetime, Visit.person_id)\
                .join(Concept, Visit.visit_concept_id==Concept.concept_id)\
                .filter(Visit.visit_occurrence_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="visit_concept_id":
        keyword = int(keyword)
        query = db.session.query(Visit.visit_occurrence_id, Concept.concept_name.label("visit_occurrence_name"), 
                Visit.visit_start_datetime, Visit.visit_end_datetime, Visit.person_id)\
                .join(Concept, Visit.visit_concept_id==Concept.concept_id)\
                .filter(Visit.visit_concept_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="visit_start_datetime":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Visit.visit_occurrence_id, Concept.concept_name.label("visit_occurrence_name"), 
                Visit.visit_start_datetime, Visit.visit_end_datetime, Visit.person_id)\
                .join(Concept, Visit.visit_concept_id==Concept.concept_id)\
                .filter(Visit.visit_start_datetime==keyword)\
                .offset(start).limit(start+many).all()
    elif column =="visit_end_datetime":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Visit.visit_occurrence_id, Concept.concept_name.label("visit_occurrence_name"), 
                Visit.visit_start_datetime, Visit.visit_end_datetime, Visit.person_id)\
                .join(Concept, Visit.visit_concept_id==Concept.concept_id)\
                .filter(Visit.visit_end_datetime==keyword)\
                .offset(start).limit(start+many).all()
    elif column == "person_id":
        keyword = int(keyword)
        query = db.session.query(Visit.visit_occurrence_id, Concept.concept_name.label("visit_occurrence_name"), 
                Visit.visit_start_datetime, Visit.visit_end_datetime, Visit.person_id)\
                .join(Concept, Visit.visit_concept_id==Concept.concept_id)\
                .filter(Visit.person_id==keyword)\
                .offset(start).limit(start+many).all()
    else:
        query = db.session.query(Visit.visit_occurrence_id, Concept.concept_name.label("visit_occurrence_name"), 
                Visit.visit_start_datetime, Visit.visit_end_datetime, Visit.person_id)\
                .join(Concept, Visit.visit_concept_id==Concept.concept_id)\
                .offset(start).limit(start+many).all()

    for row in query:
        res[cnt] = dict(row)
        cnt += 1

    return res

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