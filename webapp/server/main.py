# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging
import requests
import json
import csv

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'abc'

@app.route('/devices')
def devices():
    devices = []
    # with open('devices.csv') as csvfile:
    #     reader = csv.reader(csvfile)
    #     parameters = ['device_id', 'mac', 'manufacturer', 'category', 'allowed_count', 'not_allowed_count']
    #     for row in reader:
    #         device = {}
    #         for i in range(len(parameters)):
    #             device[parameters[i]] = row[i]
    #         devices.append(device)

    devices = [{'device_id': 1, 'mac': 2, 'manufacturer': 3, 'category': 4, 'allowed_count': 5, 'not_allowed_count': 6 }]

    device_id_packets = {}
    with open('../../data/TestFile1_output.csv') as csvfile:
        reader = csv.reader(csvfile)
        parameters = ['date', 'time', 'src_mac', 'src_ip', 'src_port',
                      'dest_mac', 'dest_ip', 'dest_port', 'protocol',
                      'is_good', 'is_allowed', 'comment']
        for row in reader:
            packet = {}
            for i in range(len(parameters)):
                packet[parameters[i]] = row[i]
            packet['device_id'] = 1
            if packet['device_id'] in device_id_packets:
                device_id_packets[packet['device_id']].append(packet)
            else:
                device_id_packets[packet['device_id']] = [packet]

    output = {'devices': []}

    for device in devices:
        device_shown_features = {
            'name': '{} {}'.format(device['manufacturer'], device['category']),
            'packets': device_id_packets[device['device_id']]
        }
        output['devices'].append(device_shown_features)

    return jsonify(output)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
