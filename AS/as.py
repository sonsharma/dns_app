# ss13449 lab 3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
import json

server_port = 53533
serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind(('', server_port))
ipmaps = {}
#function for finding request type of dns query
def dnsquery(hname, req_type):
    cont = ipmaps[req_type + ' ' + hname]
    fs_ip = cont['VALUE']
    return str(fs_ip).encode()
#function for getting hostname, ip, request type, time to live in query message
def getreq(query_message):
    message = json.loads(query_message.decode())
    ip = 'VALUE' in message
    if not ip:
        hname = message['NAME']
        req_type = message['TYPE']
        return dnsquery(hname, req_type)
    else:
        hname = message['NAME']
        ip = message['VALUE']
        req_type = message['TYPE']
        ttl = message['TTL']
        return register(hname, ip, req_type, ttl)
#function for putting hostname, ip, request type, time to live in content dictionary (gets ip address from host name)
def register(hname, ip, req_type, ttl):
    cont = {'TYPE': req_type, 'NAME': hname, 'VALUE': ip, 'TTL': ttl}
    key = req_type + ' ' + hname
    ipmaps[key] = cont
    return json.dumps('').encode()

while True:
    query_message, addr = serverSock.recvfrom(2048)
    response_message = getreq(query_message)
    serverSock.sendto(response_message, addr)
