import time

from us_bank.us_bank_base_crawler import UsBankBaseCrawler
from credential import Credential

class UsBankPrivateCrawler(UsBankBaseCrawler):
	"""Private Crawler for US Bank"""
	def __init__(self):
		UsBankBaseCrawler.__init__(self)
		self._name = "US Bank Private"

	def Crawl(self):
		try:
			credential = Credential('#', '#')
			self.Login(credential)
		except Exception as e:
			print('An error occurred in the US Bank Private Crawler: %s' % (str(e)))

		self.Browser.quit()

	def Index(self):
		Crawl()

	@property
	def Name(self):
		return self._name