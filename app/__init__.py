#
import os

from flask import Flask
from flask_restful import Api

from .routes import Docs, Stocks
#

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  api = Api(app)

  app.config.from_pyfile('config.py', silent=True)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # with app.app_context():
  #   print('within app context')

  # app.register_blueprint(test.test_bp)
  # app.register_blueprint(docs.docs_bp)

  api.add_resource(Docs.Docs, '/api/v1/docs')
  api.add_resource(Stocks.Stocks, '/api/v1/stocks/all')

  return app
