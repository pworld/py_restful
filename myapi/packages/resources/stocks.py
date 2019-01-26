import os
import requests
import numpy as np

from flask import request, Response, jsonify, Blueprint, current_app as app
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from myapi.models import User
from myapi.extensions import ma, db
from myapi.commons.pagination import paginate

class timeSeries(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def post(self):

        symbol = request.json.get('symbol', None)
        interval = request.json.get('interval', None)
        function = request.json.get('function', None)

        data = {
            'symbol'  : symbol,
            'interval' : interval,
            'analyze' : interval,
            'apikey' : os.environ.get('API_KEY'),
            'function' : function
        }

        url = os.environ.get('API_URL')
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

        r = requests.get(url, headers=headers, params=data)
        response = r.json()
        key = 'Time Series ('+interval+')'
        data = response[key]

        DataSet = []
        for key in data:
            values = []
            values.append(key)
            values.append(data[key]['1. open'])
            values.append(data[key]['2. high'])
            values.append(data[key]['3. low'])
            values.append(data[key]['4. close'])
            values.append(data[key]['5. volume'])

            DataSet.append(values)

        #df = pd.DataFrame(data = DataSet, columns=['Time','Open','High','Low','Close','Volume'])
        response = np.array(DataSet).tolist()

        return response


class stockList(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def post(self):

        keywords = request.json.get('keywords', None)
        function = request.json.get('function', None)

        data = {
            'keywords'  : keywords,
            'function' : function,
            'apikey' : os.environ.get('API_KEY')
        }

        url = os.environ.get('API_URL')
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

        r = requests.get(url, headers=headers, params=data)
        response = r.json()
        key = 'bestMatches'
        data = response[key]

        return data