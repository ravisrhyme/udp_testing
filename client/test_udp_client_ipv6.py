import socket

#IPv6 address of NLB ENI
UDP_IP = "2600:1f14:cf4:6405:7e84:10bb:566d:b41d"

#ingress source port configured in Rule
UDP_PORT = 9000

#Sample payload
MESSAGE = "Hello, World!"

#counter to number of messages
count = 0

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET6, # Internet
                     socket.SOCK_DGRAM) # UDP
while 1:
    count += 1
    print "sending message ",count
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
