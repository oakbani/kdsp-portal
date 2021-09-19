from flask import Flask
from flask import render_template
from controller import (
    khandani_sahara_api,
    sehat_health_care_api,
    taleem_aur_hunar_api,
    contact_api,
)


app = Flask(__name__, template_folder="templates")
app.register_blueprint(khandani_sahara_api)
app.register_blueprint(sehat_health_care_api)
app.register_blueprint(taleem_aur_hunar_api)
app.register_blueprint(contact_api)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
