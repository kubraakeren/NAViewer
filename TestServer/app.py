#!/usr/bin/env python
from flask import Flask, request
from receivedata import receiveData

app = Flask(__name__)

log = []

@app.route('/', methods=['GET', 'POST'])
def saveData():

	data = request.get_json(force=True)

	print request.method
	log.append(data)
	
	logfile = open("log.txt", "a+")
	logfile.write(str(log))
	logfile.close()
	# Append received data to log file.

	html = ""
	for e in log:
		html = "%s <p>%s</p>" % (html, e['dest'])

	return "%s" % html

def index():

	# TODO : render log file as html
	pass

if __name__ == '__main__':
	app.run(debug=True)
