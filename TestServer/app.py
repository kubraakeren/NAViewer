#!/usr/bin/env python
from flask import Flask, request
from receivedata import receiveData

app = Flask(__name__)

log = []

@app.route('/', methods=['GET', 'POST'])
def saveData():

	data = request.get_json(force=True) 
	with open('log.txt', 'a') as outfile:
  	  json.dump(data, outfile)
	
	return index()

def index():

	r_file = open("log.txt", "r")		
	html = ""
	for e in r_file:
		html = "%s <p>%s</p>" % (html, e[:]) 
		return "%s" % html '

if __name__ == '__main__':
	app.run(debug=True)
