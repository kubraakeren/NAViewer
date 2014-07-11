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
        <p>     </p>
        <p>===>For view write /view</p>
        <p>===>For total size write /size_sort</p>
        <p>===>For source address write /saddr_sort</p>
        <p>===>For destination address write /daddr_sort</p>
        <p>===>For destination port write /dport_sort</p>
        <p>===>For protocol write /proto_sort</p>
        """

    return response


@app.route('/view', methods=['GET'])

def index():

    activity = mongo.db.netactivity.find()

    html = '<table width="80%"><td><u><b>Time</b></u></td><td><u><b>Protocol</b></u></td><td><u><b>Source Address</b></u></td><td><u><b>Destination Address</b></u></td><td><u><b>Destination Port</b></u></td><td><u><b>Packet Size</b></u></td>'

    for record in activity:
        html = html + '<tr>'
        html = html + '<td>%s</td>' % record['time']
        html = html + '<td>%s</td>' % record['proto']
        html = html + '<td>%s</td>' % record['source']
        html = html + '<td>%s</td>' % record['dest']
        html = html + '<td>%s</td>' % record['d_port']
        html = html + '<td>%s</td>' % record['size']
        html = html + '</tr>'
    html = html + '</table>'

    response = html
                                                                                                                                                                                           13,0-1        Top
    return response
    

@app.route('/size_sort', methods=['GET'])

def size_sort():

    activity = mongo.db.netactivity.find({ 'size':{"$gt": 1 }}).sort( [('size', -1) ] )

    html = '<table width="80%"><td><u><b>Time</b></u></td><td><u><b>Protocol</b></u></td><td><u><b>Source Address</b></u></td><td><u><b>Destination Address</b></u></td><td><u><b>Destination Port</b></u></td><td><u><b>Packet Size (Sorted)</b></u></td>'

    for record in activity:
        html = html + '<tr>'
        html = html + '<td>%s</td>' % record['time']
        html = html + '<td>%s</td>' % record['proto']
        html = html + '<td>%s</td>' % record['source']
        html = html + '<td>%s</td>' % record['dest']
        html = html + '<td>%s</td>' % record['d_port']
        html = html + '<td>%s</td>' % record['size']
        html = html + '</tr>'
    html = html + '</table>'

    return html


@app.route('/saddr_sort', methods=['GET'])

def saddr_sort():

    html = '<table width="80%"><td><u><b>Source Address</b></u></td><td><u><b>Packet Size (Sorted)</b></u></td>'

    size = mongo.db.netactivity.aggregate([ { '$group': { '_id': '$source', 'Total Size': { '$sum': "$size" } } }, { '$sort': { 'Total Size': -1 } }] )

#    print size.__class__

    for record in size['result']:
        html = html + '<tr>'
        html = html + '<td>%s</td>' % record['_id']
        html = html + '<td>%s</td>' % record['Total Size']
        html = html + '</tr>'

    html = html + '</table>'

    return html
    
    
@app.route('/daddr_sort', methods=['GET'])

def daddr_sort():

    html = '<table width="80%"><td><u><b>Destination Address</b></u></td><td><u><b>Packet Size (Sorted)</b></u></td>'

    size = mongo.db.netactivity.aggregate([ { '$group': { '_id': '$dest', 'Total Size': { '$sum': "$size" } } }, { '$sort': { 'Total Size': -1 } }] )

    for record in size['result']:
        html = html + '<tr>'
        html = html + '<td>%s</td>' % record['_id']
        html = html + '<td>%s</td>' % record['Total Size']
        html = html + '</tr>'
    html = html + '</table>'

    return html

@app.route('/dport_sort', methods=['GET'])

def dport_sort():

    html = '<table width="80%"><td><u><b>Destination Port</b></u></td><td><u><b>Packet Size (Sorted)</b></u></td>'

    size = mongo.db.netactivity.aggregate([ { '$group': { '_id': '$d_port', 'Total Size': { '$sum': "$size" } } }, { '$sort': { 'Total Size': -1 } }] )

    for record in size['result']:
        html = html + '<tr>'
        html = html + '<td>%s</td>' % record['_id']
        html = html + '<td>%s</td>' % record['Total Size']
        html = html + '</tr>'
    html = html + '</table>'

    return html


@app.route('/proto_sort', methods=['GET'])

def proto_sort():

    html = '<table width="80%"><td><u><b>Protocol</b></u></td><td><u><b>Packet Size (Sorted)</b></u></td>'

    size = mongo.db.netactivity.aggregate([ { '$group': { '_id': '$proto', 'Total Size': { '$sum': "$size" } } }, { '$sort': { 'Total Size': -1 } }] )

    for record in size['result']:
        html = html + '<tr>'
        html = html + '<td>%s</td>' % record['_id']
        html = html + '<td>%s</td>' % record['Total Size']
        html = html + '</tr>'
    html = html + '</table>'

    return html


if __name__ == '__main__':
        app.run(debug=True)
