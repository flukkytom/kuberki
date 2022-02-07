#!flask/bin/python
import optparse
import os, sys, re, json, requests

from app import init_app
from flaskrun import flaskrun
from flask import jsonify

application = init_app()

WAVEBET_URL = "https://www.wavebets.com"

# predict get endpoint
@application.route('/predict', methods=['GET'])
def login():
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
