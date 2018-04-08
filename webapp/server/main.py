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
    output = {'devices':[
        {'name': 'iPhone6 #1',
         'packets': [
             {'name': '17:09 04-07 2018',
              'src_ip': 'aaa'}
         ]},
        {'name': 'Amazon Echo #1',
         'packets': [
             {'name': '17:01 04-07 2018',
              'src_ip': 'bbb'}
         ]},
    ]}

    # print("code {}\n".format(r.status_code))
    return jsonify(output)
    # print("json \n" + json.dumps(r.json()))


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
