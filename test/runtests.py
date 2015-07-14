
# APP   : MessNote Server TestCases
# author: chenxiaba
# date  : 2015.07.12

from tornado.testing import AsyncTestCase
from tornado.testing import AsyncHTTPClient
from tornado.testing import gen_test
from tornado.testing import main

import unittest

#application = tornado.web.Application([
#		(r"/", MainHandler),
#		(r"/api/v1/people/(.*)", PeopleHandler),
#		(r"/api/v1/people/(.*)/ideas", UserIdeaHandler),
#		(r"/api/v1/idea/([0-9]*)", IdeaHandler)
#	], **settings)

INDEX_URL = "http://localhost:8888"
API_URL  = "/api/v1/"
BASE_URL = INDEX_URL + API_URL

IDEA_URL = BASE_URL + "idea"

class MainTestCase(AsyncTestCase):
	"""Test index"""

	@gen_test(timeout=10)
	def test_index_fetch(self):
		client = AsyncHTTPClient(self.io_loop)
		
		resp = yield client.fetch(INDEX_URL)
		self.assertIn("hello", resp.body)


class IdeaTestCase(AsyncTestCase):
	"""Test Idea function"""

	def setUp(self):
		print "Init IdeaTestCase..."
		super(IdeaTestCase, self).setUp()
		self.saved = AsyncHTTPClient._save_configuration()

	def tearDown(self):
		print "TearDown IdeaTestCase..."
		AsyncHTTPClient._restore_configuration(self.saved)
		super(IdeaTestCase, self).tearDown()

	@gen_test(timeout=10)
	def test_idea_add(self):
		#Add
		client = AsyncHTTPClient(self.io_loop)
		
		resp = yield client.fetch(IDEA_URL)

		self.assertIn("", resp.body)


if __name__ == '__main__':
	unittest.main()


		