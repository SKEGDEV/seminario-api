from flask import Blueprint, jsonify, request
from src.utils.obj_client import obj_client
from src.auth.obj_token import token


client_routes = Blueprint('client_routes',__name__)

@client_routes.route('/create-client', methods=['POST'])
def create_client():
    set_data = request.get_json()
    user_id = token().decrypt_token(set_data['token'])
    json_response = obj_client().create_new_client(
            set_data['references'],
            set_data['dpi'],
            set_data['first_name'],
            set_data['last_name'],
            set_data['work_phone'],
            set_data['home_phone'],
            set_data['personal_phone'],
            set_data['other_phone'],
            set_data['isMarried'],
            set_data['isRented'],
            set_data['work_direction'],
            set_data['home_direction'],
            set_data['email'],
            set_data['facebook'], 
            set_data['photo'],
            user_id.get('id')
            )
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code=200
        return response
    response.status_code=500
    return response

@client_routes.route('/get-clients', methods=['POST'])
def get_clients():
    set_data=request.get_json()
    id_user =token().decrypt_token(set_data['token'])
    json_response = obj_client().get_all_clients(id_user.get('id'))
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code=200
        return response
    response.status_code=500
    return response

@client_routes.route('/get-client/<int:id>', methods=['GET'])
def get_client(id):
    json_response = obj_client().get_client_record(id)
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code=200
        return response
    response.status_code=500
    return response

