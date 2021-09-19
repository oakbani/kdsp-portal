from flask import Blueprint, request, render_template
from include.db import db_session
from include.parsers import FamilyDetailsSchema
from include.models import Family as FamilyModel

sehat_health_care_api = Blueprint(
    "sehat_health_care", __name__, url_prefix="/sehat-health-care"
)


@sehat_health_care_api.route("/")
def index():
    return render_template("sehat-health-care.html")


@sehat_health_care_api.route("/appointment")
def appointment():
    return render_template("appointment.html")


@sehat_health_care_api.route("/appointment-registration", methods=["POST", "GET"])
def appointment_registration():
    if request.method != "POST":
        return
    payload = {
        "email": request.form["email"],
        "father_name": request.form["father_name"],
        "mother_name": request.form["mother_name"],
        "father_occupation": request.form["father_occupation"],
        "mother_occupation": request.form["mother_occupation"],
        "father_contact_num": request.form["father_contact_num"],
        "mother_contact_num": request.form["mother_contact_num"],
    }
    args = FamilyDetailsSchema().load(payload)
    family = FamilyModel(**args)
    db_session.add(family)
    db_session.commit()
    return render_template("appointment.html")
