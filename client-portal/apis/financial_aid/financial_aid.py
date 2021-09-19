from flask import Blueprint, request
from include.db import db_session
from include.models import (
    Donor as DonorModel,
    FinancialAid as FinancialAidModel,
    Family as FamilyModel,
)
from include.parsers import (
    DonorRegistrationSchema,
    FinancialAidRecipientUpdateByAdminSchema,
    FinancialAidRecipientRegistrationSchema,
    FinancialAidRecipientSchema,
)

financial_aid_api = Blueprint("financial_aid", __name__, url_prefix="/financial_aid")


@financial_aid_api.route("/donor", methods=["POST"])
def add_donor():
    try:
        payload = request.get_json()
        args = DonorRegistrationSchema().load(payload)
        therapist = DonorModel(**args)
        db_session.add(therapist)
        db_session.commit()
        message = "Details Added Successfully!"
        status_code = 200
    except Exception as e:
        message = e
        status_code = 500
    return {"message": message}, status_code


@financial_aid_api.route("/donor/<id>", methods=["GET"])
def get_donor(id):
    response = {}
    try:
        query_obj = db_session.query(DonorModel).filter(DonorModel.id == id).first()
        serialized_result = DonorRegistrationSchema().dump(query_obj)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code


@financial_aid_api.route("/donor", methods=["GET"])
def get_all_donors():
    response = {}
    try:
        query_obj = db_session.query(DonorModel).all()
        serialized_result = DonorRegistrationSchema().dump(query_obj, many=True)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code


@financial_aid_api.route("/recipient", methods=["POST"])
def add_recipient():
    try:
        print("here1")
        payload = request.get_json()
        print("here2", payload)
        family_obj = (
            db_session.query(FamilyModel)
            .filter(FamilyModel.email == payload["email"])
            .first()
        )
        print("here3", family_obj.id)
        custom_args = {
            "family_id": family_obj.id,
            "family_income": payload["family_income"],
            "expenses": payload["expenses"],
        }
        args = FinancialAidRecipientRegistrationSchema().load(custom_args)
        print("here4", args)
        recipient = FinancialAidModel(**args)
        print("here5", recipient.id)
        db_session.add(recipient)
        db_session.commit()
        message = "Details Added Successfully!"
        status_code = 200
    except Exception as e:
        message = e
        status_code = 500
    return {"message": message}, status_code


@financial_aid_api.route("/recipient/<id>", methods=["GET"])
def get_recipient(id):
    response = {}
    try:
        query_obj = (
            db_session.query(FinancialAidModel)
            .filter(FinancialAidModel.id == id)
            .first()
        )
        serialized_result = FinancialAidRecipientSchema().dump(query_obj)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code


@financial_aid_api.route("/recipient/<id>", methods=["PUT"])
def add_financial_aid_result(id):
    response = {}
    try:
        payload = request.get_json()
        query_obj = (
            db_session.query(FinancialAidModel)
            .filter(FinancialAidModel.id == id)
            .first()
        )
        args = FinancialAidRecipientUpdateByAdminSchema().load(payload)
        query_obj.eligible_for_aid = args["eligible_for_aid"]
        db_session.commit()
        serialized_result = FinancialAidRecipientSchema().dump(query_obj)
        response["data"] = serialized_result
        response["message"] = "success"
        status_code = 200
    except Exception as e:
        response["message"] = e
        status_code = 500
    return response, status_code
