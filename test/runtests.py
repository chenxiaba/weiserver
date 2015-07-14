
# APP   : MessNote Server TestCases
# author: chenxiaba
# date  : 2015.07.12

from tornado.testing import AsyncTestCase
from tornado.testing import AsyncHTTPClient
from tornado.testing import gen_test
from tornado.testing import main

import unittest

BASE_URL = "http://localhost:8888"

class MainTestCase(AsyncTestCase):
	"""Test index"""

	@gen_test(timeout=10)
	def test_index_fetch(self):
		client = AsyncHTTPClient(self.io_loop)
		
		resp = yield client.fetch(BASE_URL)
		self.assertIn("hello", resp.body)


if __name__ == '__main__':
	unittest.main()


		