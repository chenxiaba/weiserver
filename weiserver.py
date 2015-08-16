# APP   : Messnote Server v0.1
# author: chenxiaba
# date  : 2015.07.11
import os
import json

import torndb

import tornado.ioloop
import tornado.web
from  tornado.web import RequestHandler
from pymongo import MongoClient

def resp(module, status=True, info=None):
	""" Dump a common resp for request """
	resp_json = {
		"module" : module,
		"status" : status
	}

	if type(info) is dict:
		data["info"] = json.dumps(info)

	elif type(info) is str:
		data["info"] = info
	else:
		raise Exception("Function<resp>: %s: Unsupport type" % module)

	return json.dumps(info)

class MainHandler(RequestHandler):
	def get(self):
		data = {}
		data["hello"] = "Hello"
		data["name"] = "weiserver"
		self.write(data)


class IdeaHandler(RequestHandler):
	"""Handle msg of one user"""
	def get(self, idea_id):
		if idea_id:
			idea = db.ideas.find({"_id": idea_id})
		else:
			idea = db.ideas.find()

		self.write(str(idea))


	def post(self, usr_id):
		""" New idea """
		#new idea
		idea = json.loads(self.request.body)

		if not checkinfo(idea):
			self.write(resp(self.__name__, False, 
				"Idea info is not right"))


		msg["user"] = usr_id
		db.ideas.insert(msg)
		
		#TODO: update stat table

		self.set_header("Content-Type", "application/json")
		self.set_status(201)
		self.write(resp(self.__name__, True))

	def put(self, idea_id):
		"""Update a messge"""
		pass

	def delete(self, idea_id):
		"""Delete a idea"""

		idea = db.ideas.remove(
			{"_id": ObjectId(str(idea_id))}
			)
		
		self.write(resp(self.__name__, True))

	def checkinfo(self, data):
		return True

		
# mongodb env
MONGODB_DB_URL = os.environ.get('AWS_MONGO_DB_URL') if os.environ.get('AWS_MONGO_DB_URL') else 'mongodb://localhost:27017/'
MONGODB_DB_NAME = os.environ.get('AWS_APP_NAME') if os.environ.get('AWS_APP_NAME') else 'messnote'

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]


settings = {
	"template_path": os.path.join(os.path.dirname(__file__),"templates"),
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"debug": True
}	


application = tornado.web.Application([
		(r"/", MainHandler),
		(r"/api/v1/idea/([0-9]*)", IdeaHandler)
	], **settings)


if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()