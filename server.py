from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from person.controller import personController

db_host = input("[DB HOST] : ")
db_port = input("[DB port] : ")
db_name = input("[DB name] : ")
db_user = input("[DB user] : ")
db_password = input("[DB password] : ")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
db = SQLAlchemy(app)

app.register_blueprint(personController.person_api, url_prefix="/person")

if __name__ == '__main__':
    app.run(debug=True)