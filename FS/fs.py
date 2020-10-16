#ss13449 lab 3 submission
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_api import status
import json
from socket import *
app = Flask(__name__)
@app.route('/fib', methods = ['GET'])
#function for generating fibonacci series
def calfib_n(n):
    n = int(n)
    if n <= 2:
        return 1
    return calfib_n(n-1) + calfib_n(n-2)
def fib():
    n = request.args['number']
    result = calfib_n(n)
    return str(result)

@app.route('/register', methods = ['PUT'])
#function for getting hostname, ip, port, request type from content dictionary and send it to client socket
def register():
    cont = request.get_json()
    hname = cont.get('hostname')
    ip = cont.get('ip')
    as_ip = cont.get('as_ip')
    as_port = int(cont.get('as_port'))
    register_json = {'TYPE': 'A', 'NAME': hname, 'VALUE': ip, 'TTL': 10}
    clientsckt = socket(AF_INET, SOCK_DGRAM)
    clientsckt.sendto(json.dumps(register_json).encode(), (as_ip, as_port))
    response_message, server_add = clientsckt.recvfrom(2048)
    return 'successfully registered', status.HTTP_201_CREATED
app.run(host='0.0.0.0',port=9090,debug=True)
