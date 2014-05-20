# NAViewer (Network Activity Viewer)

The purpose of NAViewer is to provide web based visualition portal for Local Area Network (LAN) Activity.

System components are;

 * Data provider agent for client nodes,
 * Web server application to process data and serve gui,
 * Database model to store collected data.
    
## Data Provider Agent

Data Provider Agent will collect and post network traffic data to web server. Following data will be provided by each network packet captured by the agent:

 * Receive Time,
 * Packet Type,
 * Source IP Address,
 * Destination IP Address,
 * Destination Port,
 * Packet Length.

Data Provider Agent may be a bash script, or a python program.

Following command demonstrates how to collect desired data from command line:

```
# tcpdump -tt -n -S net 10.1.1.0/24
```

## Web Server

Web server will have two basic functions:

 * Web service for agents to post collected data,
 * Graphical User Interface (GUI) for users to view network activity.

Using one of the following frameworks are mandatory for the web server:

 * Node.js,
 * Django,
 * CherryPy,
 * Flask

### Web Service

Web service should allow network traffic information from multiple data provider agents to be submitted. Received data should be stored into a database.

JSON format should be used for network data. So, following example is given for a client data packet:

An ARP packet:
```json
{
	"time" : "1400571514.320004",
	"type" : "ARP",
	"src_addr" : "10.1.1.32",
	"dst_addr" : "0.0.0.0",
	"dst_port" : -1,
	"length" : 46
}
```

An IP packet:
```json
{
	"time" : "1400571514.687267",
	"type" : "IP",
	"src_addr" : "10.1.1.172",
	"dst_addr" : "10.1.1.255",
	"dst_port" : 1947,
	"length" : 40
}
```

### Web GUI

Web GUI should be able to display,

 * Overall network activity,
 * Activity for a single client,
 * Most active clients,
 * Some discrimination for Local/Remote network addresses.

Activity display should be updated in real-time (asynchronously). 

## Database Model

Purpose of application is monitoring, not logging. So, database should not expand with time, but only with addresses. However, a time buffer will be needed just to display some past activity graph.

Above circumstances should be considered during database model design.

## Development Environment Rules

 * All python scripts should run in ```virtualenv```. 
 * Git should be actively used for version control, not just with bulk commits for critical milestones.
 * Personal editor and IDE preferences should not be committed in.
 * Any intermediate or generated files should not be committed in.