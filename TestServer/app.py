#!/usr/bin/env python
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		# Save Data : This code is for POST only, not for viewing from browser.

		# Get posted network activity from request body.
		data = request.get_json(force=True)
		# Open server-side log file and append received activity.
		logfile = open("log.txt", "a")
		logfile.write(str(data))
		logfile.close()
		# Inform posting client that everything is fine.
		response = "ok"

	elif request.method == 'GET':
		# View Data : This code is for viewing accumulated data from browser.

		# Open server-side log file.
		r_file = open("log.txt", "r")
		# Generate a simple html view from its contents.
		html = ""
		for e in r_file:
			html = "%s <p>%s</p>" % (html, e)

		# Return it for viewing inside browser.
		response = html

	return response

if __name__ == '__main__':
	app.run(debug=True)

