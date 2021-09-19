from flask import Blueprint, request
from include.db import db_session
from include.models import Therapist as TherapistModel
from include.parsers import TherapistDetailsSchema


therapist_api = Blueprint("therapist", __name__, url_prefix="/therapist")


@therapist_api.route("/", methods=["POST"])
def add_therapist():
    try:

        payload = request.get_json()
        args = TherapistDetailsSchema().load(payload)
        therapist = TherapistModel(**args)
        db_session.add(therapist)
        db_session.commit()
        message = "Details Added Successfully!"
        status_code = 200
    except Exception as e:
        message = e
        status_code = 500
    return {"message": message}, status_code


@therapist_api.route("/<id>", methods=["GET"])
def get_therapist(id):
    response = {}
    try:
        query_obj = (
            db_session.query(TherapistModel).filter(TherapistModel.id == id).first()
        )
        serialized_result = TherapistDetailsSchema().dump(query_obj)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code


@therapist_api.route("/<id>", methods=["PUT"])
def edit_therapist_details(id):
    response = {}
    try:
        payload = request.get_json()
        query_obj = (
            db_session.query(TherapistModel).filter(TherapistModel.id == id).first()
        )
        args = TherapistDetailsSchema().load(payload)
        query_obj.name = args["name"]
        query_obj.contact_num = args["contact_num"]
        db_session.commit()
        serialized_result = TherapistDetailsSchema().dump(query_obj)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code
