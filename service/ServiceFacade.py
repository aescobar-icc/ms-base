from service.ServiceImp import ServiceImp

from flask import request,Response
from bson.json_util import dumps
import json

class ServiceFacade:

	@staticmethod
	def echo():
		postJson = request.json
		res = ServiceImp.echo(postJson)
		return Response(
					response=json.dumps(res),
					status=200, 
					mimetype="application/json"
		)
	