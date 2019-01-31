import os
import json
import numpy as np

from flask import request, Response, jsonify, Blueprint, current_app as app
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from myapi.models import User
from myapi.extensions import ma, db
from myapi.packages.helpers import (
    analyze_data,
    apiRequests,
    listOrder,
    show_data,
    saveProcess
)

class timeSeriesSave(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def post(self):

        symbol = request.json.get('symbol', None)
        interval = request.json.get('interval', None)
        function = request.json.get('function', None)
        analyze = request.json.get('analyze', None)
        save = request.json.get('save', None)

        data = {
            'symbol'  : symbol,
            'interval' : interval,
            'analyze' : analyze,
            'apikey' : os.environ.get('API_KEY'),
            'function' : function,
            'save' : save,
        }

        response = apiRequests(data)
        key = 'Time Series ('+interval+')'
        data = response[key]

        DataSet = listOrder(data)

        stock_type = {'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5}
        col = stock_type[analyze]

        response = show_data(DataSet[1],col)
        response['type'] = analyze
        response['start_time'] = DataSet[0][0]
        response['end_time'] = DataSet[0][-1]
        response['interval'] = interval

        return response

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

        response = apiRequests(data)
        key = 'Time Series ('+interval+')'
        data = response[key]

        DataSet = listOrder(data)

        stock_type = {'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5}
        col = stock_type[analyze]

        response = analyze_data(DataSet[1],stock_type,analyze_type,col)

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

        response = apiRequests(data)

        key = 'bestMatches'
        data = response[key]

        return data