import os
from service.ServiceImp import ServiceImp

class TestServiceImp:
	# def init(self):
	# 	os.environ['MEMCACHE_HOST'] = 'ms-memcached'
	# 	os.environ['MEMCACHE_PORT'] = '11211'

	def test_echo(self):
		data = {"mean":23, "median":25, "mode":30}
		resp = ServiceImp.echo(data)
		assert resp == data