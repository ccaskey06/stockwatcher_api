#
from flask import jsonify
from flask_restful import Resource, request
#

class Docs(Resource):
  def get(self):
    # print(request.args)
    return jsonify('Documentation')
