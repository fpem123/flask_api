from flask import Blueprint, request
import person.model.personModel as model

person_api = Blueprint('person_api', __name__)

##
#   환자 테이블의 row를 조회
@person_api.route("/", methods=["GET"])
def visit_search():
    try:
        column = request.args.get('column', type=str, default="all")
        keyword = request.args.get('keyword', type=str, default="")
        start = request.args.get('start', type=int, default=0)
        many = request.args.get('many', type=int, default=10)
    except Exception as e:
        return {"result": "error"}, 400
        
    try:
        res = model.person_row_search(column, keyword, start, many)

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400


##
#   전체 환자 수를 반환
@person_api.route("/all", methods=["GET"])
def person_count():
    try:
        res = model.person_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400


##
#   성별별 환자 수를 반환
@person_api.route("/gender", methods=["GET"])
def person_gender_count():
    try:
        res = model.person_gender_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400


##
#   인종별 환자 수를 반환
@person_api.route("/race", methods=["GET"])
def person_race_count():
    try:
        res = model.person_race_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400


##
#   민족별 환자 수를 반환
@person_api.route("/ethnicity", methods=["GET"])
def person_ethnicity_count():
    try:
        res = model.person_ethnicity_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400


##
#   사망 환자 수를 반환
@person_api.route("/death", methods=["GET"])
def person_death_count():
    try:
        res = model.person_death_count()

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400