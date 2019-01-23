from flask import Blueprint
from flask_restful import Api

from myapi.packages.resources import stockList


blueprint = Blueprint('app', __name__, url_prefix='/app')
app = Api(blueprint)


app.add_resource(stockList, '/stock-list')
