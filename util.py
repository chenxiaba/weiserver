# Some util functions
# Author: chenxiaba
# Date  : 2015.07.10

def json_loads(data):
	try:
		data = json.loads(data)
		return data

	except Exception, e:
		print "Response is not right:%s" %data
		return None