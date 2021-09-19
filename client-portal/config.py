import json, os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/config.json") as config_file:
    config = json.load(config_file)

SECRET_KEY = config.get("SECRET_KEY")
DB_NAME = config.get("DB_NAME")
DB_PORT = config.get("DB_PORT")
DB_USER = config.get("DB_USER")
DB_PASS = config.get("DB_PASS")
DB_HOST = config.get("DB_HOST")
