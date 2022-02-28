from flask import Blueprint, request
from person.domain.personDomain import Person

person_api = Blueprint('person_api', __name__)

@person_api.route("/", methods=["GET"])
def person_count():
    try:
        gender = request.args.get('gender', type=int, default=None)
        race = request.args.get('race', type=int, default=None)
        ethnicity = request.args.get('ethnicity', type=int, default=None)
        death = request.args.get('death', type=int, default=None)
    except:
        return {"result": "error"}, 400

    try:
        query = Person.query

        if gender:
            query = query.filter(Person.gender_concept_id == gender)
        if race:
            query = query.filter(Person.race_concept_id == race)
        if ethnicity:
            query = query.filter(Person.ethnicity_concept_id == ethnicity)
        if death:
            pass

        query = query.count()

        return {"result": query}, 200
    except:
        return {"result": "error"}, 400