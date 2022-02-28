from flask import Flask
from person.controller import personController

app = Flask(__name__)

app.register_blueprint(personController.person_api, url_prefix="/person")

if __name__ == '__main__':
    app.run(debug=True)