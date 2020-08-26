class UtilReflection:

	@staticmethod
	def get_value(obj,path):
		path = path.split(".")
		rec=''
		for key in path:
			try:
				rec+=key
				obj=obj[key]
				
			except Exception as e:
				raise Exception('dict: %s do not contain key : "%s"'%(str(obj),rec))
			
		return obj