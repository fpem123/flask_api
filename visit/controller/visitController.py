from flask import Blueprint, request
import visit.model.visitModel as model

visit_api = Blueprint('visit_api', __name__)


##
#   방문 테이블의 row를 조회
@visit_api.route("/", methods=["GET"])
def visit_search():
    try:
        column = request.args.get('column', type=str, default="all")
        keyword = request.args.get('keyword', type=str, default="")
        start = request.args.get('start', type=int, default=0)
        many = request.args.get('many', type=int, default=10)
    except Exception as e:
        return {"result": "error"}, 400
        
    try:
        res = model.visit_row_search(column, keyword, start, many)

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400


##
#   방문 유형별 방문수를 반환
@visit_api.route("/visit", methods=["GET"])
def visit_concept_count():
    try:
        res = model.visit_concept_count()

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400


##
#   환자 성별별 방문 수를 반환
@visit_api.route("/gender", methods=["GET"])
def visit_gender_count():
    try:
        res = model.visit_gender_count()

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400


##
#   환자 인종별 방문수를 반환
@visit_api.route("/race", methods=["GET"])
def visit_race_count():
    try:
        res = model.visit_race_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400


##
#   환자 인종별 방문수를 반환
@visit_api.route("/ethnicity", methods=["GET"])
def visit_ethnicity_count():
    try:
        res = model.visit_ethnicity_count()

        return {"result": res}, 200
    except:
        return {"result": "error"}, 400
