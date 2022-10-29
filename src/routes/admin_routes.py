from src.utils.obj_admin import admin
from flask import Blueprint, jsonify

admin_route = Blueprint('admin_route', __name__)

@admin_route.route('/get-users', methods=['GET'])
def get_users():
    json_response = admin().get_all_users()
    response = jsonify(json_response)
    if(not json_response.get('err')): 
        response.status_code = 200
        return response
    response.status_code =500
    return response
        
@admin_route.route('/get-user/<int:id>', methods=['GET'])
def get_user(id):
    json_response = admin().get_user_record(id)
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code = 200
        return response
    response.status_code = 500
    return response

@admin_route.route('/disable-user/<int:id>', methods=['DELETE'])
def disable(id):
    json_response = admin().disable_user(id)
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code = 200
        return response
    response.status_code = 500
    return response

@admin_route.route('/get-user-update/<int:id>', methods=['GET'])
def get_user_update(id):
    json_response = admin().get_user_update(id)
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code = 200
        return response
    response.status_code = 500
    return response

@admin_route.route('/get-users-disable', methods=['GET'])
def get_users_disable():
    json_response = admin().get_users_disable()
    response = jsonify(json_response)
    if(not json_response.get('err')): 
        response.status_code = 200
        return response
    response.status_code =500
    return response

@admin_route.route('/enable-user/<int:id>', methods=['DELETE'])
def enable(id):
    json_response = admin().enable_user(id)
    response = jsonify(json_response)
    if(not json_response.get('err')):
        response.status_code = 200
        return response
    response.status_code = 500
    return response
