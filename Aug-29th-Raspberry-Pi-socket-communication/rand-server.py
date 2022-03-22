#!/usr/bin/env python
# -*- coding:utf-8 -*-

# rand-server.py
import socket
import time
import smbus
import sys
import RPi.GPIO as GPIO

# Init I2C
bus = smbus.SMBus(1)
address = 0x20
# define host ip: RPi's IP
HOST_IP = "192.168.137.244"
HOST_PORT = 8888
print("Starting socket: TCP...")

# 1.Create socket object: socket = socket.socket(family, type)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT))
host_addr = (HOST_IP, HOST_PORT)

# 2.bind socket to addr:socket.bind(address)
socket_tcp.bind(host_addr)

# 3.listen connection request: socket.listen(backlog)
socket_tcp.listen(1)

# 4.wait for client: connection, address = socket.accept()
socket_con, (client_ip, client_port) = socket_tcp.accept()
print("Connection accepted from %s." %client_ip)
socket_con.send("Welcome to RPi TCP server!")

# 5.handle
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
    try:
        print("Receiving package...")
        data = socket_con.recv(512)
        if len(data) > 0:
            if data == '1':
                num = bus.read_byte(address)
                print("Received:1, get rand number %d" %num)
                time.sleep(1)
                socket_con.send(str(num)) # socket data must be string
            elif data == '0':
                print("Received:0, exit")
                GPIO.output(11, GPIO.LOW)
                socket_con.close()
            # time.sleep(1)
            continue
    except Exception as e:
        print type(e)
        print e.args
        print e
        socket_tcp.close()
        sys.exit(1)
