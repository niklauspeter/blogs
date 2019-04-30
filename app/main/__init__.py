from flask import Blueprint

# Initializing application
main = Blueprint('main', __name__)
from . import views, errors
