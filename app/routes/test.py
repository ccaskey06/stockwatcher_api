#
from flask import Blueprint, current_app, escape, flash, g, redirect, render_template, request, session, url_for

test_bp = Blueprint('auth', __name__)

@test_bp.route('/', methods=['GET'])
def home():
  return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
