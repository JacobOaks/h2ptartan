from flask import jsonify, request, url_for, g, abort
from app import db
from app.api import bp
from app.models import Car

@bp.route('/cars', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'cMake' not in data or 'cModel':
        return bad_request('must include make and model')
    if User.query.filter_by(email=data['model']).first():
        return bad_request('please use a different model')
    car = Car()

    car.from_dict(data, new_car=True)
