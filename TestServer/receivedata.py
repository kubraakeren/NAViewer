import socket, sys
from struct import *

def receiveData():

	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

	packet = s.recvfrom(65536)

	packet = packet[0]

	ip_header = packet[0:20]

	iph = unpack('!2B3H2BH4s4s' , ip_header)   

	t_length = iph[2]
	protocol = iph[6]

	s_addr = socket.inet_ntoa(iph[8]);
	d_addr = socket.inet_ntoa(iph[9]);

	protocol_s = protocol   

	if protocol == 1:
		protocol_s = 'ICMP'
	if protocol == 6:
		protocol_s = 'TCP'
	if protocol == 17:
		protocol_s = 'UDP'

	tcp_header = packet[20:40]

	tcph = unpack('!HHLLBBHHH' , tcp_header)

	dest_port = tcph[1]       

	data = { 
		'proto' : protocol_s,
		'source' : str(s_addr),
		'dest' : str(d_addr),
		'd_port' : str(dest_port),
		'size' : str(t_length)
	}

	return data

