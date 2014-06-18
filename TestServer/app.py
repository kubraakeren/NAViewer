#!/usr/bin/env python
from flask import Flask, request
from receivedata import receiveData

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def saveData():

	#data = request.get_json(force=True) | BadRequest hatasini almamak icin bu kismi asagidaki gibi yazdim
	data = receiveData()	
	logfile = open("log.txt", "a")
	logfile.write(str(data))
	logfile.close()
	
	return index()
	
def index():
	
	r_file = open("log.txt", "r")
	html = ""
	for e in r_file:
		html = "%s <p>%s</p>" % (html, e[:]) ##Postlama islemi veri kaybetmeden calisiyor fakat html formati olarak duzenleme kisminda tam olarak istedigimi elde edemedim.
		return "%s" % html 

if __name__ == '__main__':
	app.run(debug=True)

