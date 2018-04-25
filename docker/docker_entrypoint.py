#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Check to see if postgress db is up yet or delays
import socket
import time


def check_server(address, port):
    # Create a TCP socket
    s = socket.socket()
    print("Attempting to connect to %s on port %s" % (address, port))
    try:
        s.connect((address, port))
        print("Connected to %s on port %s" % (address, port))
        return True
    except (socket.error, ConnectionRefusedError):
        print("Connection to %s on port %s failed" % (address, port))
        return False


if __name__ == '__main__':
    for i in range(1, 10):
        if check_server('db', 5432):
            print("Found DB continuing")
            break
        else:
            print("Couldn't find DB in attempt %s delaying %s seconds" % (i, i))

            time.sleep(i)
    print("Continuing start up regardless")