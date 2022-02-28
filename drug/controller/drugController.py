from flask import Blueprint, request
import drug.model.drugModel as model

drug_api = Blueprint('drug_api', __name__)

@drug_api.route("/", methods=["GET"])
def drug_search():
    try:
        column = request.args.get('column', type=str, default="all")
        keyword = request.args.get('keyword', type=str, default="")
        start = request.args.get('start', type=int, default=0)
        many = request.args.get('many', type=int, default=10)
    except Exception as e:
        return {"result": "error"}, 400

    try:
        res = model.drug_row_search(column, keyword, start, many)

        return {"result": res}, 200
    except Exception as e:
        print(e)
        return {"result": "error"}, 400