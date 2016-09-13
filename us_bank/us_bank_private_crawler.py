import time
import logging
import requests

from us_bank.us_bank_base_crawler import UsBankBaseCrawler
from us_bank.pages.issuers import IssuersPage
from credential import Credential

class UsBankPrivateCrawler(UsBankBaseCrawler):
	"""Private Crawler for US Bank"""
	def __init__(self):
		UsBankBaseCrawler.__init__(self)
		self._name = "US Bank Private"
		self._allDealsPageUrl = 'https://trustinvestorreporting.usbank.com/TIR/public/deals/?layout=layout'

	def _crawlIssuers(self):
		logging.debug('Crawling Issuers on url %s' % self._allDealsPageUrl)
		self.Browser.get(self._allDealsPageUrl)
		html = (self.Browser.page_source).encode('utf-8')		
		issuerPage = IssuersPage(html)
		issuerPage.Parse()
		issuers = issuerPage.Issuers
		for issuer in issuers:
			print('%s' % issuer.Name)
		

	def Crawl(self):
		logging.info('Crawling %s' % self._name)
		try:
			credential = Credential('#', '#')			
			loggedIn = self.Login(credential)
			if(loggedIn == True):
				self._crawlIssuers()
			
		except Exception as e:
			logging.error('An error occurred in the %s Crawler: %s' % (self._name, str(e)))

		self.Browser.quit()

	def Index(self):
		pass

	@property
	def Name(self):
		return self._name