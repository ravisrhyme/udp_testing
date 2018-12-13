import socket

#public IPv4 adress of NLB ENI
UDP_IP = "10.0.184.224"

#Ingress source port configured in rule
UDP_PORT = 9000

#Sample payload to send
MESSAGE = "Hello, World!"

#number of packets sent
count = 0

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
while 1:
    count += 1
    print "sending message ",count
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
