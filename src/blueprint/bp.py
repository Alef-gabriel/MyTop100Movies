from flask import Blueprint

#Create blueprint
bp = Blueprint('bp', __name__)

#first route
@bp.route('/')
def index():
    return ''

