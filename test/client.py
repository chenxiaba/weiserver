#A http client used for REST Test
# Author: chenxiaba
# Date  : 2015.07.11

import urllib2
import json


host = 'http://localhost:8888/'
DEBUG = True

def display(info):
	if DEBUG:
		print info

def http_get(url):
	resp = urllib2.urlopen(url)

	data = resp.read()
	display(data)
	return data

def http_post(url, content):
	data = json.dumps(content)

	req = urllib2.Request(url, data)
	resp = urllib2.urlopen(req)

	rsp_data = resp.read()
	display(rsp_data)
	return rsp_data

def http_put(url, content):
	data = json.dumps(content)

	req = urllib2.Request(url, data)
	req.add_header("Content-Type", "application/json")
	req.get_method = lambda:'PUT'

	resp = urllib2.urlopen(req)

	rsp_data = resp.read()
	display(rsp_data)
	return rsp_data

def http_delete(url, content):
	data = json.dumps(content)

	req = urllib2.Request(url, data)
	req.add_header("Content-Type", "application/json")
	req.get_method = lambda:'DELETE'

	resp = urllib2.urlopen(req)

	rsp_data = resp.read()
	display(rsp_data)
	return rsp_data

