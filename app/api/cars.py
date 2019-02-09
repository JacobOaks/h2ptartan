from flask import jsonify, request, url_for, g, abort
from app import db
from app.api import bp
from app.models import Car
from app.api.errors import bad_request

@bp.route('/cars', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    print(data)
    if 'cMake' not in data or 'cModel' not in data:
        return bad_request('must include make and model')
    if Car.query.filter_by(cModel=data['cModel']).first():
        return bad_request('please use a different model')
    car = Car()

    car.from_dict(data, new_car=True)
    db.session.add(car)
    db.session.commit()
    response = jsonify(car.to_dict())
    response.status_code = 201
    return response
