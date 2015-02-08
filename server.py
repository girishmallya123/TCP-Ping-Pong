#! /usr/local/bin/python

import socket
import threading
import struct


def main():
    print "creating socket"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print "binding socket to localhost"
    server_socket.bind(("localhost", 8765))

    print "listening"
    server_socket.listen(5)

    client_num = 0
    while True:
        #accept connections from outside
        print "waiting for a client to connect..."
        (clientsocket, address) = server_socket.accept()
        #now do something with the clientsocket
        #in this case, we'll pretend this is a threaded server

        t = threading.Thread(target=handleClient, args=(clientsocket, client_num))
        t.run()

        client_num += 1


def handleClient(socket, ident):
    data = socket.recv(4)
    print "Attempting to unpack a python struct - {}".format(data)
    (msg,) = struct.unpack("i", data)
    print "decoded '{0}'".format(msg)

    print "Reading {0} more bytes".format(msg)
    data = socket.recv(int(msg))
    print data




if __name__ == "__main__":
    main()
