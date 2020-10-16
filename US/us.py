#ss13449 lab 3 submission
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
import requests
from flask_api import status
from socket import *
import json
app = Flask(__name__)
#function for getting ip, port, hname in query json dictionary and send it to client socket
@app.route('/fib', methods = ['GET'])
def qauthserver(as_ip, as_port, hname):
    clientsckt = socket(AF_INET, SOCK_DGRAM)
    query_json = {'TYPE': 'A', 'NAME': hname}
    clientsckt.sendto(json.dumps(query_json).encode(), (as_ip, as_port))
    ip_add, server_add = clientsckt.recvfrom(2048)
    return ip_add.decode()

#function for getting hname, ip, request type, port from request arguments
def accept_request():
    hname = request.args['hname']
    fs_port = request.args['fs_port']
    as_ip = request.args['as_ip']
    as_port = int(request.args['as_port'])
    n = request.args['n']
    if hname == '' or fs_port == '' or as_ip == '' or as_port == '' or n == '' or not n.isdigit():
        return 'bad format', status.HTTP_400_BAD_REQUEST
    fs_ip = qauthserver(as_ip, as_port, hname)
    real_add = 'http://' + fs_ip + ':' + fs_port
    dict_to_send_1 = {'n': n}
    result = requests.get(real_add + '/fib', params=dict_to_send_1)
    return result.text, status.HTTP_200_OK
app.run(host='0.0.0.0',port=8080,debug=True)