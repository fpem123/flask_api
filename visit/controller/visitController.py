from flask import Blueprint, request
import visit.model.visitModel as model

visit_api = Blueprint('visit_api', __name__)

@visit_api.route("/visit", methods=["GET"])
def visit_concept_count():
    try:
        res = model.visit_concept_count()

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400


@visit_api.route("/gender", methods=["GET"])
def visit_gender_count():
    try:
        res = model.visit_gender_count()

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400


@visit_api.route("/race", methods=["GET"])
def visit_race_count():
    try:
        res = model.visit_race_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400


@visit_api.route("/ethnicity", methods=["GET"])
def visit_ethnicity_count():
    try:
        res = model.visit_ethnicity_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400