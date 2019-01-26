from flask import Blueprint
from flask_restful import Api

from myapi.packages.resources import stockList, timeSeries, stockList


blueprint = Blueprint('app', __name__, url_prefix='/app')
app = Api(blueprint)

app.add_resource(stockList, '/stock-list')
app.add_resource(timeSeries, '/time-series')