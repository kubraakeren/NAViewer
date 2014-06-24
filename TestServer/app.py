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

    html = '<table width="80%">'
    for record in activity:
        html = html + '<tr>'
        html = html + '<td>%s</td>' % record['proto']
        html = html + '<td>%s</td>' % record['source']
        html = html + '<td>%s</td>' % record['dest']
        html = html + '</tr>'
    html = html + '</table>'

    response = html

    return response

if __name__ == '__main__':
	app.run(debug=True)
