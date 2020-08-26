#from lib.database.DBConnection  import DBConnection
#from lib.database.mongodb.UtilMongo  import UtilMongo

from core.exceptions.ExceptionApi import ExceptionApi
from core.log.UtilLog import UtilLog

class ServiceImp:
	
	@staticmethod
	def echo(data):
		UtilLog.debug('echo service')
		UtilLog.debug(data)
		if "error_test" in data and data["error_test"] == True:
			raise ExceptionApi(500,"error test",error_code="error_test")
		return data
	