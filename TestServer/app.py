#!/usr/bin/env python
import json
from flask import Flask, request
from receivedata import receiveData

app = Flask(__name__)

log = []

@app.route('/', methods=['GET', 'POST'])
def saveData():

    if request.method == 'POST':

        data = request.get_json(force=True)
        with open('log.txt', 'a') as outfile:
            line = json.dumps(data) + '\n'
            outfile.write(line)

        response = 'ok'

    elif request.method == 'GET':

        print "GET"

        response = """
        <p>This URL used to post data from clients.</p>
        """

    return response

@app.route('/view', methods=['GET'])
def index():

    lines = []
    try:
        with open("log.txt", "r") as fp:
            lines = fp.readlines()

        html = ''
        for line in lines:
            html = '%s<p>%s</p>\n' % (html, line)

        response = html

    except IOError:
        response = """
        <p>Unable to open log file.
        """

    return response

if __name__ == '__main__':
	app.run(debug=True)
