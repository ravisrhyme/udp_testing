#!/usr/bin/python

import socket
import sys
import getopt
import time
import errno

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "d:p:i:l:")
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--destIP"):
            destIP = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-i", "--interval"):
            interval = int(arg)
        elif opt in ("-l", "--length"):
            length = int(arg)
        else:
            assert False, "unhandled option"
    msg = "Hello World"
    var = 0
    interval = 10
    length = 1

    while var < length:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto(msg,(destIP, port))
      data, server = s.recvfrom(100)
      print data
      time.sleep(interval)
      var = var + 1
      s.close()

if __name__ == "__main__":
    main(sys.argv[1:])


