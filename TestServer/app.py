#!/usr/bin/env python
import json
from flask import Flask, request
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def saveData():

    if request.method == 'POST':

        data = request.get_json(force=True)

        mongo.db.netactivity.insert(data)

        response = 'ok'

    elif request.method == 'GET':

        print "GET"

        response = """
        <p>This URL is reserved for posting data from clients.</p>
        """

    return response

@app.route('/view', methods=['GET'])
def index():

    activity = mongo.db.netactivity.find()

    html = ''
    for record in activity:
        html = '%s<p>%s</p>\n' % (html, record)

    response = html

    return response

if __name__ == '__main__':
	app.run(debug=True)
