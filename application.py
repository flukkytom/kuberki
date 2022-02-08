#!flask/bin/python
import optparse
import os, sys, re, json, requests
from flask import jsonify, Flask

# from app import init_app
from flaskrun import flaskrun

application = Flask(__name__)

WAVEBET_URL = "https://www.wavebets.com"

# predict get endpoint
@application.route('/predict', methods=['GET'])
def predict():
    """
    Call Wavebets.com Prediction URL
    """
    url = "{}/wavebets/stakii/predictions".format(WAVEBET_URL)
    # Call Wavebets API
    response = requests.get(url, verify=False)

    data = response.json()
    print(data, file=sys.stderr)

    return jsonify(data)


if __name__ == '__main__':
    flaskrun(application)
