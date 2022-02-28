import flask_sqlalchemy
from sqlalchemy.sql.expression import func
from death.domain.deathDomain import Death
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

def death_row_search(column, keyword, start, many):
    res = {}
    cnt = 0

    if column =="person_id":
        keyword = int(keyword)
        query = db.session.query(Death.person_id, Death.death_date)\
                .filter(Death.person_id == keyword)\
                .offset(start).limit(start+many).all()
    elif column =="death_date":
        keyword = datetime.strptime(keyword, "%Y-%m-%d").date()
        query = db.session.query(Death.person_id, Death.death_date)\
                .filter(Death.death_date == keyword)\
                .offset(start).limit(start+many).all()
    else:
        query = db.session.query(Death.person_id, Death.death_date)\
                .offset(start).limit(start+many).all()

    for row in query:
        res[cnt] = dict(row)
        cnt += 1

    return res
