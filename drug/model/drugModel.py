import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from drug.domain.drugDomain import Drug
from concept.domain.conceptDomain import Concept
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

def drug_row_search(column, keyword, start, many):
    res = {}
    cnt = 0

    if column =="person_id":
        keyword = int(keyword)
        query = db.session.query(Drug.person_id, Concept.concept_name.label("drug_concept_name"), 
                Drug.drug_exposure_start_datetime, Drug.drug_exposure_end_datetime, Drug.visit_occurrence_id)\
                .join(Concept, Drug.drug_concept_id==Concept.concept_id)\
                .filter(Drug.person_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="condition_concept_id":
        keyword = int(keyword)
        query = db.session.query(Drug.person_id, Concept.concept_name.label("drug_concept_name"), 
                Drug.drug_exposure_start_datetime, Drug.drug_exposure_end_datetime, Drug.visit_occurrence_id)\
                .join(Concept, Drug.drug_concept_id==Concept.concept_id)\
                .filter(Drug.drug_concept_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="condition_start_datetime":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Drug.person_id, Concept.concept_name.label("drug_concept_name"), 
                Drug.drug_exposure_start_datetime, Drug.drug_exposure_end_datetime, Drug.visit_occurrence_id)\
                .join(Concept, Drug.drug_concept_id==Concept.concept_id)\
                .filter(Drug.drug_exposure_start_datetime==keyword)\
                .offset(start).limit(start+many).all()
    elif column =="condition_end_datetime":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Drug.person_id, Concept.concept_name.label("drug_concept_name"), 
                Drug.drug_exposure_start_datetime, Drug.drug_exposure_end_datetime, Drug.visit_occurrence_id)\
                .join(Concept, Drug.drug_concept_id==Concept.concept_id)\
                .filter(Drug.drug_exposure_end_datetime==keyword)\
                .offset(start).limit(start+many).all()
    elif column == "visit_occurrence_id":
        keyword = int(keyword)
        query = db.session.query(Drug.person_id, Concept.concept_name.label("drug_concept_name"), 
                Drug.drug_exposure_start_datetime, Drug.drug_exposure_end_datetime, Drug.visit_occurrence_id)\
                .join(Concept, Drug.drug_concept_id==Concept.concept_id)\
                .filter(Drug.visit_occurrence_id==keyword)\
                .offset(start).limit(start+many).all()
    else:
        query = db.session.query(Drug.person_id, Concept.concept_name.label("drug_concept_name"), 
                Drug.drug_exposure_start_datetime, Drug.drug_exposure_end_datetime, Drug.visit_occurrence_id)\
                .join(Concept, Drug.drug_concept_id==Concept.concept_id)\
                .offset(start).limit(start+many).all()

    for row in query:
        res[cnt] = dict(row)
        cnt += 1

    return res
