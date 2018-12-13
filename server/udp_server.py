#!/usr/bin/python

import socket
import sys
import getopt
import time
import errno

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "p:m:")
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-m", "--message"):
            msg = arg
        else:
            assert False, "unhandled option"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 9000
    message = "server hello"
    s.bind(('10.0.184.226',port))
    while True:
      message, address = s.recvfrom(100)
      print message
      print address
      s.sendto(msg,address)

if __name__ == "__main__":
    main(sys.argv[1:])

