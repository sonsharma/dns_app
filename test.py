#ss13449 lab 3 submission
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#details provided are
#   "hostname": "fibonacci.com"
#   "ip": "0.0.0.0"
#   "as_ip": "0.0.0.0"
#   "as_port": "53533"

import requests
#code to send the generic dictionary
send_dict = {"hostname": "fibonacci.com", "ip": "0.0.0.0", "as_ip": "0.0.0.0", "as_port": "53533"}
fs_ip = 'http://0.0.0.0'
fs_port = '9090'
fs_add = fs_ip + ':' + fs_port + '/register'
r = requests.put(fs_add, json=send_dict)
print(r.text)
#code to send the  dictionary having number 5
send_dict = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 5}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
r = requests.get(us_add, params=send_dict)
print(r.text)
#code to send the  dictionary having number 9
send_dict = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 9}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
r = requests.get(us_add, params=send_dict)
print(r.text)
#code to send the  dictionary having number X
send_dict = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 'X'}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
r = requests.get(us_add, params=send_dict)
print(r.text)