from flask import Blueprint, request, render_template
from include.db import db_session
from include.models import RoleTypes, Account as AccountModel, Role as RoleModel
from include.parsers import AccountRegistrationSchema, AccountLoginSchema
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import Forbidden, Unauthorized, NotFound

account_api = Blueprint("account", __name__, url_prefix="/account")


@account_api.route("/signup", methods=["POST"])
def signup():
    payload = request.get_json()
    role = (
        db_session.query(RoleModel)
        .filter_by(title=RoleTypes[payload["role"]].value)
        .first()
    )
    payload["role_id"] = role.id
    payload.pop("role")
    args = AccountRegistrationSchema().load(payload)
    user = db_session.query(AccountModel).filter_by(email=args["email"]).first()
    if user:
        return {"message": "User already exist!"}, 409
    args["password"] = generate_password_hash(args["password"], method="sha256")
    new_obj = AccountModel(**args)

    db_session.add(new_obj)
    db_session.commit()

    return "", 200


@account_api.route("/signin", methods=["POST"])
def signin():
    payload = request.get_json()

    args = AccountLoginSchema().load(payload)

    user = db_session.query(AccountModel).filter_by(email=args["email"]).first()

    if not user or not check_password_hash(user.password, args["password"]):
        raise Unauthorized

    auth_token = user.encode_auth_token(user.id)

    return {"auth_token": auth_token}, 200
