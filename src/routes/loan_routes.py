from flask import Blueprint, jsonify, request
from src.utils.obj_loan import obj_loan

loan_route = Blueprint('loan_route', __name__)

@loan_route.route('/get-proyection', methods=['POST'])
def proyection():
    set_data = request.get_json()
    json_response = obj_loan().generate_loan_proyection(
             set_data["init_amount"],
             set_data["quote_amount"],
             set_data["interest"],
             set_data["first_payment_date"],
             set_data["payment_frecuency"],
             set_data["type_interest"]
            )
    response = jsonify(json_response)
    response.status_code = 200
    return response

@loan_route.route('/create-loan', methods=['POST'])
def create_loan():
    set_data = request.get_json() 
    json_response =obj_loan().create_loan(
        set_data["client_id"],
        set_data["amount"],
        set_data["quote"],
        set_data["car_photo"],
        set_data["house_photo"],
        set_data["first_payment_date"],
        set_data["interest"],
        set_data["period_payment"],
        set_data["interest_type"]
        ) 
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code =200
        return response
    response.status_code=500
    return response

@loan_route.route('/get-all-clients', methods=["GET"])
def get_clients():
    json_response = obj_loan().get_all_clients()
    response = jsonify(json_response)
    if(not json_response.get("err")):
        response.status_code = 200
        return response
    response.status_code =500
    return response
