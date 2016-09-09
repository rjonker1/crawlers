
import abc
from config import *
from selenium import webdriver
from pages import UsBankHomePage

BASE_URL = 'trustinvestorreporting.usbank.com'
HOST =  "trustinvestorreporting.usbank.com"

class UsBankBaseCrawler(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self):

		self._pAndIFactorFileName = 'P & I Factors'
		self._owaspTokenName = 'OWASP_CSRFTOKEN'
		self._allDealsPage = 'https://trustinvestorreporting.usbank.com/TIR/public/deals/?layout=layout'
		self._domainWhenLoggedIn ='"https://trustinvestorreporting.usbank.com'

		self._browser = webdriver.PhantomJS(PHANTOMJS_PATH, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
		self._browser.set_window_size(1120, 550)
		self._browser.get(BASE_URL)

	#@abc.abstractMethod
	def Login(self, credential):
		homePage = UsBankHomePage(self._browser)
		if(homePage.IsValidLoginPage() == False):
			return False

		try:
			loginResult = homePage.Login(credential.UserName, credential.Password)
			if(loginResult == False):
				return
		except:
			return False

		return True