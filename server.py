from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from person.controller import personController
from visit.controller import visitController
from concept.controller import conceptController
from condition.controller import conditionController
from drug.controller import drugController
from death.controller import deathController

db_host = input("[DB HOST] : ")
db_port = input("[DB port] : ")
db_name = input("[DB name] : ")
db_user = input("[DB user] : ")
db_password = input("[DB password] : ")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
db = SQLAlchemy(app)

app.register_blueprint(personController.person_api, url_prefix="/person")
app.register_blueprint(visitController.visit_api, url_prefix="/visit")
app.register_blueprint(conceptController.concept_api, url_prefix="/concept")
app.register_blueprint(conditionController.condition_api, url_prefix="/condition")
app.register_blueprint(drugController.drug_api, url_prefix="/drug")
app.register_blueprint(deathController.death_api, url_prefix="/death")

if __name__ == '__main__':
    app.run(debug=True)