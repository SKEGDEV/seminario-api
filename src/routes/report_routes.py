from flask import Blueprint, jsonify, request
from src.utils.obj_pdf import obj_report as report
from src.utils.help_list import obj_list


report_route = Blueprint('report_route', __name__)

@report_route.route('/create-proyection-pdf', methods=['POST'])
def proyection_pdf():  
    set_data = request.get_json()
    obj_list.append({
        "proyection":set_data["proyection"],
        "total":set_data["total"]
        })
    return jsonify({"msm":"generando pdf...", "url":"http://192.168.1.10:5000/report/get-proyection"}) 

@report_route.route('/get-proyection', methods=["GET"])
def get_proyection():
    for data in obj_list:
        response = report().proyection_pdf(data["proyection"], data["total"]) 
        obj_list.clear()
        return response
