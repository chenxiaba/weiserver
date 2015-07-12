import tornado.ioloop
import tornado.web
from  tornado.web import RequestHandler

class MainHandler(RequestHandler):
	def get(self):
		data = {}
		data["hello"] = "hello"
		data["name"] = "word"
		self.write(data)

class MsgHandler(RequestHandler):
	"""docstring for MsgHandler"""
	def get(self, name):
		data = {}
		data["hello"] = "hello"
		data["name"] = "%s"%name
		self.write(data)

settings = {
	"template_path": os.path.join(os.path.dirname(__file__),"templates"),
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"debug": True
}	

application = tornado.web.Application([
		(r"/", MainHandler),
		(r"/msg/([a-z]*)", MsgHandler)
	], **settings)


if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()