from flask import Blueprint, jsonify, request
import concept.model.conceptModel as model

concept_api = Blueprint('concept_api', __name__)

##
#   concept_id 정보 테이블 검색
@concept_api.route("/", methods=["GET"])
def visit_concept_count():
    try:
        search = request.args.get('search', type=str, default="id")
        keyword = request.args.get('keyword', type=str, default="")
        start = request.args.get('start', type=int, default=0)
        many = request.args.get('many', type=int, default=10)
    except Exception as e:
        return {"result": "error"}, 400

    try:
        res = model.concept_info(search, keyword, start, many)

        return jsonify(res), 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 500