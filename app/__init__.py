#
import os

from flask import Flask

from .routes import test
#

def create_app():
  app = Flask(__name__, instance_relative_config=True)

  app.config.from_pyfile('config.py', silent=True)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # with app.app_context():
  #   print('within app context')

  app.register_blueprint(test.test_bp)

  return app
