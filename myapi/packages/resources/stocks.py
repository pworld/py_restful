import os
import requests
import pandas as pd
import simplejson as json

from flask import request, Response, jsonify, Blueprint, current_app as app
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
        return {"msg": "try post"}

    def post(self):
        return {"msg": "try post"}

class timeSeries(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def get(self):
        return {"msg": "try post"}

    def post(self):

        data = {
            'symbol'  : request.json.get('symbol', None),
            'interval' : request.json.get('interval', None),
            'apikey' : os.environ.get('API_KEY'),
            'function' : 'TIME_SERIES_INTRADAY'
        }

        url = os.environ.get('API_URL')
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

        response = Response(requests.get(url, headers=headers, params=data))
        #df =  json.loads(response)
        #df = json.loads(response.decode("utf-8"))
        #import pdb; pdb.set_trace()
        return response

class timeSeriesCSV(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def get(self):
        return {"msg": "try post"}

    def post(self):

        data = {
            'symbol'  : request.json.get('symbol', None),
            'interval' : request.json.get('interval', None),
            'apikey' : os.environ.get('API_KEY'),
            'function' : 'TIME_SERIES_INTRADAY',
            'datatype' : 'csv'
        }

        url = os.environ.get('API_URL')
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

        response = Response(requests.get(url, headers=headers, params=data))

        #df = pd.read_csv(pd.compat.BytesIO(response.encode('UTF-8')), header='timestamp,open,high,low,close,volume')
        #df = pd.read_csv(pd.compat.StringIO(response), header='timestamp,open,high,low,close,volume')
        #import pdb; pdb.set_trace()
        return response