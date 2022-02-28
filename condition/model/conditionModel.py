import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from condition.domain.conditionDomain import Condition
from concept.domain.conceptDomain import Concept
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

def condition_row_search(column, keyword, start, many):
    res = {}
    cnt = 0

    if column =="person_id":
        keyword = int(keyword)
        query = db.session.query(Condition.condition_occurrence_id, Condition.person_id, Concept.concept_name, 
            Condition.condition_start_datetime, Condition.condition_end_datetime, Condition.visit_occurrence_id)\
                .join(Concept, Condition.condition_concept_id==Concept.concept_id)\
                .offset(start).limit(start+many).all()
    elif column =="condition_concept_id":
        keyword = int(keyword)
        query = db.session.query(Condition.condition_occurrence_id, Condition.person_id, Concept.concept_name, 
            Condition.condition_start_datetime, Condition.condition_end_datetime, Condition.visit_occurrence_id)\
                .join(Concept, Condition.condition_concept_id==Concept.concept_id)\
                .filter(Condition.condition_concept_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="condition_start_datetime":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Condition.condition_occurrence_id, Condition.person_id, Concept.concept_name, 
            Condition.condition_start_datetime, Condition.condition_end_datetime, Condition.visit_occurrence_id)\
                .join(Concept, Condition.condition_concept_id==Concept.concept_id)\
                .filter(Condition.condition_start_datetime==keyword)\
                .offset(start).limit(start+many).all()
    elif column =="condition_end_datetime":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Condition.condition_occurrence_id, Condition.person_id, Concept.concept_name, 
            Condition.condition_start_datetime, Condition.condition_end_datetime, Condition.visit_occurrence_id)\
                .join(Concept, Condition.condition_concept_id==Concept.concept_id)\
                .filter(Condition.condition_end_datetime==keyword)\
                .offset(start).limit(start+many).all()
    elif column == "visit_occurrence_id":
        keyword = int(keyword)
        query = db.session.query(Condition.condition_occurrence_id, Condition.person_id, Concept.concept_name, 
            Condition.condition_start_datetime, Condition.condition_end_datetime, Condition.visit_occurrence_id)\
                .join(Concept, Condition.condition_concept_id==Concept.concept_id)\
                .filter(Condition.visit_occurrence_id==keyword)\
                .offset(start).limit(start+many).all()
    else:
        query = db.session.query(Condition.condition_occurrence_id, Condition.person_id, Concept.concept_name, 
            Condition.condition_start_datetime, Condition.condition_end_datetime, Condition.visit_occurrence_id)\
                .join(Concept, Condition.condition_concept_id==Concept.concept_id)\
                .offset(start).limit(start+many).all()

    for row in query:
        res[cnt] = dict(row)

    return res
