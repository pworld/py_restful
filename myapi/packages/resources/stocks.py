from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from myapi.models import User
from myapi.extensions import ma, db
from myapi.commons.pagination import paginate


class stockList(Resource):
    """test get and post
    """
    method_decorators = [jwt_required]

    def get(self):
        return {"msg": "try get"}

    def post(self):
        return {"msg": "try post"}

class stockTimeSeries(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def get(self):
        """ 
        """
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        data = {
            'symbol'  : request.json.get('symbol', None),
            'interval' : request.json.get('interval', None),
            'key' : 'YWIHL1WV597UVSAU',
            'function' : 'TIME_SERIES_INTRADAY'
        }
        js = json.dumps(data)

        resp = Response(js, status=200, mimetype='application/json')
        resp.headers['Link'] = '//www.alphavantage.co/query'
        return resp

    def post(self):
        return {"msg": "try post"}