import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from concept.domain.conceptDomain import Concept

db = flask_sqlalchemy.SQLAlchemy()

def concept_info(search, keyword, start, many):
    res = {}

    if search == "name":
        keyword = f'%{keyword}%'
        query = db.session.query(Concept).filter(Concept.concept_name.like(keyword))\
            .offset(start).limit(start + many).all()
    elif search == "domain":
        keyword = f'%{keyword}%'
        query = db.session.query(Concept).filter(Concept.domain_id.like(keyword))\
            .offset(start).limit(start + many).all()
    else:
        try:
            keyword = int(keyword)
        except:
            keyword = 1

        query = db.session.query(Concept).filter(Concept.concept_id == keyword)\
            .offset(start).limit(start + many).all()

    for row in query:
        row = row.__dict__
        res[row['concept_id']] = {'concept_name': row['concept_name'], 
            'domain_id': row['domain_id']}
    
    return res