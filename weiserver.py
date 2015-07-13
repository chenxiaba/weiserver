# APP   : Messnote Server v0.1
# author: chenxiaba
# date  : 2015.07.11
import os
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
		data["hello"] = "hello"
		data["name"] = "weiserver"
		self.write(data)

class PeopleHandler(RequestHandler):
	"""Handle people info"""
	def get(self, usr_id):
		me = db.peoples.find(
				{"uid" : usr_id}
			)

		self.set_header("Content-Type", "application/json")

		if not len(me):
			self.write(resp(self.__name__, False, "Pepole not exist."))

		self.write(resp(self.__name__, True, me[0]))
		pass

	def post(self, usr_id):
		if not usr_id:
			#new people
			people = json.loads(self.request.body)
			
			if self.checkinfo(people):
				#produce a uid for people
				people["uid"] = "*****"

				db.peoples.insert(people)

				self.write(resp(
					self.__name__, True,
					{"uid": people["uid"]}
					))

			else:
				self.write(resp(
					self.__name__, False, 
					"Format is not right")
				)
		
		# unsupport
		self.write(resp(
			self.__name__, False, 
			"Unsupport method")
			)


	def put(self):
		pass

	def delete(self):
		pass

	def checkinfo(people):
		""" Check info """
		if not people:
			return False

		if "name" not in people:
			return False

		if "avatar" not in people:
			return False

		if "tag" not in people:
			return False

		if "info" not in people:
			return False

		return True

class UserIdeaHandler(RequestHandler):
	"""Get all ideas"""
	def get(self, usr_id):
		ideas = db.ideas.find(
			{"uid": usr_id}
			)

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(ideas))
	
	def post(self):
		pass

class IdeaHandler(RequestHandler):
	"""Handle msg of one user"""
	def get(self, idea_id):
		idea = db.ideas.find({"_id": idea_id})
		
		if not len(idea):
			self.write(resp(self.__name__, False, "Idea not exist"))

		self.write(json.dumps(idea[0]))

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
		(r"/api/v1/people/(.*)", PeopleHandler),
		(r"/api/v1/people/(.*)/ideas", UserIdeaHandler),
		(r"/api/v1/idea/([0-9]*)", IdeaHandler)
	], **settings)


if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()