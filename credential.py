class Credential(object):
	def __init__(self, username, password):
		self._username = username
		self._password = password

	@property
	def UserName(self):
		return self._username

	@property
	def Password(self):
		return self._password