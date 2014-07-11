import socket, sys, struct
from time import time

def receiveData():

        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

        packet = s.recvfrom(65536)

        packet = packet[0]

        ip_header = packet[0:20]

        iph = struct.unpack('!2B3H2BH4s4s' , ip_header)

        total_length = iph[2]
        protocol_number = iph[6]

        source_address = socket.inet_ntoa(iph[8]);
        destination_address = socket.inet_ntoa(iph[9]);

        if protocol_number == 1:
                protocol_id = 'ICMP'
        if protocol_number == 6:
                protocol_id = 'TCP'
        if protocol_number == 17:
                protocol_id = 'UDP'

        tcp_header = packet[20:40]

        tcph = struct.unpack('!HHLLBBHHH' , tcp_header)

        destination_port = tcph[1]

        current_time = time()

        data =  {
                'time' : current_time,
                'proto' : protocol_id,
                'source' : source_address,
                'dest' : destination_address,
                'd_port' : destination_port,
                'size' : total_length
                }

        return data
