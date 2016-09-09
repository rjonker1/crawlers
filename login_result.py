import sys

class LoginResult:
	def __init__(self, browser):
		self._notifyCredentialSourceOfFailure = True
		self._success = False

	@property
	def Success(self):
		return _success