class Debugger(object):

	"""This is a debugger class written 
	with the intention of not having to always comment out print statments
	"""

	def __init(self):
		self.flag = False

	def enable(self):
		self.flag = True

	def disable(self):
		self.flag = False

	def isEnabled(self):
		return self.flag

	def printMsg(self, message):
		if self.flag:
			print message
		else:
			pass