class Debugger(object):
	"""This is a debugger class written 
	with the intention of not having to always comment out print statments
	"""

	def __init(self, debug=False):
		self.debug = debug

	def debug(self, message):

		if self.debug:
			print message
		else:
			pass