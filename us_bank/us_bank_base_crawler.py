import abc
from config import *
from selenium import webdriver
from us_bank.pages.home import UsBankHomePage
from screenshot_capture import ScreenshotCapture
from selenium.webdriver.support.events import EventFiringWebDriver

BASE_URL = 'http://trustinvestorreporting.usbank.com'
HOST =  "http://trustinvestorreporting.usbank.com"

class UsBankBaseCrawler(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self):
		self._driver = webdriver.PhantomJS(PHANTOMJS_PATH, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

		# self._pAndIFactorFileName = 'P & I Factors'
		# self._owaspTokenName = 'OWASP_CSRFTOKEN'
		# self._allDealsPage = 'https://trustinvestorreporting.usbank.com/TIR/public/deals/?layout=layout'
		# self._domainWhenLoggedIn ='"https://trustinvestorreporting.usbank.com'

		self._browser = EventFiringWebDriver(self._driver, ScreenshotCapture('UsBank'))
		self._browser.set_window_size(1120, 550)
		self._browser.get(BASE_URL)

	#@abc.abstractMethod
	def Login(self, credential):		
		homePage = UsBankHomePage(self._browser)
		if(homePage.IsValidLoginPage() == False):
			print('Invalid Login Page')
			return False

		try:
			loginResult = homePage.Login(credential.UserName, credential.Password)			
			if(loginResult == False):
				print('login result is false')
				return False
		except Exception as e:
			print('An error occurred logging in from US Bank Base: %s' % (str(e)))
			raise

		print('Login successfull')
		return True

	@property
	def Browser(self):
		return self._browser