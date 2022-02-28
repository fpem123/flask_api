import imp
from flask import Blueprint
from person.domain.personDomain import Person

person_api = Blueprint('person_api', __name__)

@person_api.route("/", methods=["GET"])
def person_count():
    return 1