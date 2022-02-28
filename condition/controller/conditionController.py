from flask import Blueprint, request
import condition.model.conditionModel as model

condition_api = Blueprint('condition_api', __name__)

@condition_api.route("/", methods=["GET"])
def condition_search():
    try:
        column = request.args.get('column', type=str, default="all")
        keyword = request.args.get('keyword', type=str, default="")
        start = request.args.get('start', type=int, default=0)
        many = request.args.get('many', type=int, default=10)
    except Exception as e:
        return {"result": "error"}, 400

    try:
        res = model.condition_row_search(column, keyword, start, many)

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400