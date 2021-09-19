from include.models import Contact as ContactModel
from include.parsers import ContactSchema
from include.db import db_session
from flask import Blueprint, request, render_template


contact_api = Blueprint("contact", __name__, url_prefix="/contact")


@contact_api.route("/", methods=["GET"])
def index():
    return render_template("/contact.html")


@contact_api.route("/form", methods=["POST", "GET"])
def contact_form():
    if request.method != "POST":
        return
    payload = {
        "name": request.form["name"],
        "email": request.form["email"],
        "message": request.form["message"],
    }
    args = ContactSchema().load(payload)
    contact = ContactModel(**args)
    db_session.add(contact)
    db_session.commit()
    return render_template("/contact.html")
