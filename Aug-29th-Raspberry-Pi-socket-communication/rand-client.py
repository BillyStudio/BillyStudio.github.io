#!/usr/bin/env python
# -*- coding:utf-8 -*-

# rand-client.py
import socket
import time
import sys

# RPi's IP
SERVER_IP = "192.168.137.244"
SERVER_PORT = 8888

print("Starting socket: TCP...")
server_addr = (SERVER_IP, SERVER_PORT)

# 1. create socket object: socket=socket.socket(family,type)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        # 2. connect socket
        socket_tcp.connect(server_addr)
        print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
        break
    except Exception:
        print("Can't connect to server, try it later!")
        time.sleep(1)
        continue

while True:
    try:
        data = socket_tcp.recv(512)
        if len(data) > 0:
            print("Received: %s" % data)
            command = raw_input("Please input 1 or 0 to turn on/off getting rand:")
            socket_tcp.send(command)
            #time.sleep(1)
            continue
    except Exception:
        socket_tcp.close()
        socket_tcp = None
        sys.exit(1)
