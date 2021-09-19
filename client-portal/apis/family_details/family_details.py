from flask import Blueprint, request, render_template
from flask.wrappers import Response
from include.db import db_session
from include.models import Family as FamilyModel
from include.parsers import FamilyDetailsSchema
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import Forbidden, Unauthorized, NotFound


family_details_api = Blueprint("family_details", __name__, url_prefix="/family_details")


@family_details_api.route("/", methods=["POST"])
def add_family_details():
    try:

        payload = request.get_json()
        args = FamilyDetailsSchema().load(payload)
        family = FamilyModel(**args)
        db_session.add(family)
        db_session.commit()
        message = "Details Added Successfully!"
        status_code = 200
    except Exception as e:
        message = e
        status_code = 500
    return {"message": message}, status_code


@family_details_api.route("/<id>", methods=["GET"])
def get_family_details(id):
    response = {}
    try:
        query_obj = db_session.query(FamilyModel).filter(FamilyModel.id == id).first()
        serialized_result = FamilyDetailsSchema().dump(query_obj)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code


@family_details_api.route("/<id>", methods=["PUT"])
def edit_family_details(id):
    response = {}
    try:
        payload = request.get_json()
        query_obj = db_session.query(FamilyModel).filter(FamilyModel.id == id).first()
        args = FamilyDetailsSchema().load(payload)
        query_obj.email = args["email"]
        query_obj.father_name = args["father_name"]
        query_obj.mother_name = args["mother_name"]
        query_obj.father_occupation = args["father_occupation"]
        query_obj.mother_occupation = args["mother_occupation"]
        query_obj.father_contact_num = args["father_contact_num"]
        query_obj.mother_contact_num = args["mother_contact_num"]
        db_session.commit()
        serialized_result = FamilyDetailsSchema().dump(query_obj)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code
