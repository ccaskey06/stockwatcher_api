#
from flask import jsonify
from flask_restful import Resource, request
#

class Stocks(Resource):
  def get(self):
    # print(request.args)
    return jsonify({ 'ticker': 'AAPL', 'price': 100 })
