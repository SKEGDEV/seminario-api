from flask import Blueprint, request, jsonify
from src.utils.obj_auth import obj_auth

auth = Blueprint('auth', __name__)

@auth.route('/create-user', methods=['POST'])
def create():
    data = request.get_json()
    json = obj_auth().create_User(
            data['user_name'],
            data['user_password'],
            data['first_name'],
            data['last_name'],
            data['birthday'],
            data['email'],
            data['phone'],
            data['nit'],
            data['rol']
            ) 
    if not json.get('err'):
        response = jsonify(json)
        response.status_code = 200
        return response
    response = jsonify(json)
    response.status_code=500
    return response

@auth.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    json = obj_auth().get_user(data['user_name'],data['user_password'])
    if(not json.get('err')):
        response = jsonify(json)
        response.status_code = 200
        return response
    response = jsonify(json)
    response.status_code =500
    return response

@auth.route('/update-user', methods=['PUT'])
def update_user():
    data = request.get_json()
    json = obj_auth().update_user(
             data['id_user'],
             data['user_name'],
             data['user_password'],
             data['first_name'],
             data['last_name'],
             data['birthday'],
             data['email'],
             data['phone'],
             data['nit'],
             data['rol']
            ) 
    if not json.get('err'):
        response = jsonify(json)
        response.status_code = 200
        return response
    response = jsonify(json)
    response.status_code=500
    return response
    
@auth.route('/authorize-user', methods=['POST'])
def auth_user():
    data = request.get_json()
    json = obj_auth().authorize_user(data['user_name'],data['user_password'])
    if(not json.get('err')):
        response = jsonify(json)
        response.status_code = 200
        return response
    response = jsonify(json)
    response.status_code =500
    return response
        

