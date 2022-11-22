import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.partidos_blueprint import partidos_blueprints

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(partidos_blueprints)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Hello"}
    return jsonify(response)


# config  and execution code
def load_file_config():
    with open('config.json', "r") as config:
        data = json.load(config)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
