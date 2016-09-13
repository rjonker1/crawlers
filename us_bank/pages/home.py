import sys
import requests
import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class UsBankHomePage:
	def  __init__(self, browser):
		self._browser = browser
		self._statusCode = 404
		self._authenticationFailedError = False
		self._html = requests.get(browser.current_url)
		self._soup = BeautifulSoup(self._html.content, 'html.parser')	

	def IsValidLoginPage(self):
		userNameTag = self._soup.findAll('input', id='uname')
		if(len(userNameTag) == 0):
			logging.error('Login page does NOT have uname element')
			return False
		logging.debug('Login page is valid')
		return True

	def _checkForAuthenticationFailedError(self):
		logging.debug('Checking for authentication failed error')
		html = requests.get(self._browser.current_url)
		homePageHtml = BeautifulSoup(html.content, 'html.parser')
		authenticationFailed = homePageHtml.find(text='Error 403: AuthenticationFailed')
		self._authenticationFailedError = authenticationFailed is not None and len(authenticationFailed.contents) > 0

	def Login(self, username, password):
		logging.debug('Login in using %s' % (self._browser.current_url))		
		self._checkForAuthenticationFailedError()
		logging.debug('Has Auth Error %s' % (self._authenticationFailedError))
		if (self._authenticationFailedError == True):
			logging.error('Page has authentication error')
			return False

		logging.debug('login to page with username %s and password %s' % (username, password))

		self._browser.find_element_by_id('uname').clear()
		self._browser.find_element_by_id('pword').clear()

		self._browser.find_element_by_id('uname').send_keys(username)
		self._browser.find_element_by_id('pword').send_keys(password)
		self._browser.find_element_by_xpath('//input[@value="Log In"]').click()

		try:
			error = self._browser.find_element_by_xpath('//h6[@class="error"]')
			if(error is not None and len(error.contents) > 0):
				logging.error('An error occurred logging in')
				return False
		except NoSuchElementException:
			return True

		return True

	@property
	def HasAuthenticationFailedError(self):
		return self._authenticationFailedError