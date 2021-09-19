from flask import Blueprint, request, render_template
from include.models import (
    Donor as DonorModel,
    Family as FamilyModel,
    FinancialAid as FinancialAidModel,
)
from include.parsers import (
    DonorRegistrationSchema,
    FinancialAidRecipientRegistrationSchema,
)
from include.db import db_session


khandani_sahara_api = Blueprint(
    "khandani_sahara", __name__, url_prefix="/khandani-sahara"
)


@khandani_sahara_api.route("/")
def index():
    return render_template("khandani-sahara.html")


@khandani_sahara_api.route("/donor")
def donor():
    return render_template("/donor-signup.html")


@khandani_sahara_api.route("/donor/signup", methods=["POST", "GET"])
def sign_up_donor():
    if request.method == "POST":
        payload = {"name": request.form["name"], "contact_num": request.form["phone"]}
        args = DonorRegistrationSchema().load(payload)
        donor = DonorModel(**args)
        db_session.add(donor)
        db_session.commit()
        return render_template("/donor-signup.html")


@khandani_sahara_api.route("/recipient")
def recipient():
    return render_template("/recipient-signup.html")


@khandani_sahara_api.route("/recipient/signup", methods=["POST", "GET"])
def sign_up_recipient():
    if request.method == "POST":
        family_obj = (
            db_session.query(FamilyModel)
            .filter(FamilyModel.email == request.form["email"])
            .first()
        )
        custom_args = {
            "family_id": family_obj.id,
            "family_income": request.form["family_income"],
            "expenses": request.form["expenses"],
        }
        args = FinancialAidRecipientRegistrationSchema().load(custom_args)
        recipient = FinancialAidModel(**args)
        db_session.add(recipient)
        db_session.commit()
        return render_template("/recipient-signup.html")
