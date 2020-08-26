from core.regex.UtilRegex import UtilRegex

import os
class SysEnv:

	@staticmethod
	def get(env_name,def_val={},parser=None):
		val = os.environ.get(env_name)
		default_pass = def_val is not SysEnv.get.__defaults__[0]
		#print('env_name:%s def_val:%s val:%s  default_pass:%s'%(env_name,def_val,val,default_pass))
		#print(SysEnv.get.__defaults__)

		if not val and not default_pass:
			raise Exception('ENVIOREMENT VAR %s is not defined'%env_name)
		if not val :
			return def_val
		if parser:
			val = parser(val)
		return val

	@staticmethod
	def getUrl(env_name,def_val={}):
		urlText =	SysEnv.get(env_name,def_val)
		urlRegx = '(https?):\/\/((.*?)(:(\d*))?)(\/.*)'
		groups = UtilRegex.all_groups(urlRegx,urlText)

		if len(groups) == 0:
			raise Exception('env_name: %s = "%s" is not valid url'%(env_name,urlText))

		return {
			'protocol':groups[0],
			'host':groups[1],
			'hostname':groups[2],
			'port':groups[4],
			'path':groups[5]
		}
	
	@staticmethod
	def getWithPrefix(prefix):
		"""
		Get all environ names that start with 'prefix'
		"""
		envNames = []
		for envName in os.environ:
			if envName.startswith(prefix) :
				envNames.append(envName)
		return envNames