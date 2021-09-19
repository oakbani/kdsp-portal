from flask import Blueprint, request, render_template


taleem_aur_hunar_api = Blueprint(
    "taleem_aur_hunar", __name__, url_prefix="/taleem-aur-hunar"
)


@taleem_aur_hunar_api.route("/")
def index():
    return render_template("taleem-aur-hunar.html")
