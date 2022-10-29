from flask import Blueprint, jsonify, request
from src.utils.obj_payment import obj_payment

payment_route = Blueprint('payment_route', __name__)

@payment_route.route('/get-dashboard/<string:init>/<string:finish>')
def dashboard(init,finish):
    json = obj_payment().get_dashboard(init,finish) 
    response = jsonify(json)
    if(not json.get('err')):
        response.status_code = 200
        return response
    response.status_code =500
    return response

@payment_route.route('/get-history/<int:id>', methods=['GET'])
def history(id):
    json_response = obj_payment().get_history(id)
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code=200
        return response
    response.status_code=500
    return response

@payment_route.route('/get-payment/<int:id>', methods=['GET'])
def payment(id):
    json_response = obj_payment().get_payment_info(id)
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code =200
        return response
    response.status_code = 500 
    return response

@payment_route.route('/create-payment', methods=['POST'])
def create_payment():
    set_data = request.get_json()
    json_response = obj_payment().create_payment(
             set_data["loan"],
             set_data["client"],
             set_data["quote"],
             set_data["amount"],
             set_data["interestv"],
             set_data["interestt"],
             set_data["date"],
             set_data["period"]
            )
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code =200
        return response
    response.status_code =500
    return response


'''
loan:,
client:,
quote:,
amoutn:,
interestv:,
interestt:,
date:,
period:
'''
