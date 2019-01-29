import os
import json
import requests
import numpy as np

from flask import request, Response, jsonify, Blueprint, current_app as app
from flask_restful import Resource
from flask_jwt_extended import jwt_required

import time
from datetime import datetime

from myapi.models import User
from myapi.extensions import ma, db
from myapi.packages.helpers import (
    analyze_data
)

class timeSeries(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def post(self):

        symbol = request.json.get('symbol', None)
        interval = request.json.get('interval', None)
        function = request.json.get('function', None)
        analyze = request.json.get('analyze', None)
        analyze_type = request.json.get('analyze_type', None)

        data = {
            'symbol'  : symbol,
            'interval' : interval,
            'analyze' : analyze,
            'analyze_type' : analyze_type,
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
            values.append(time.mktime(datetime.strptime(key, "%Y-%m-%d %H:%M:%S").timetuple()))
            values.append(float(data[key]['1. open']))
            values.append(float(data[key]['2. high']))
            values.append(float(data[key]['3. low']))
            values.append(float(data[key]['4. close']))
            values.append(float(data[key]['5. volume']))

            DataSet.append(values)

        stock_type = {'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5}
        col = stock_type[analyze]

        response = analyze_data(DataSet,stock_type,analyze_type,col)

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