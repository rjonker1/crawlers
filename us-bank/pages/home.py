import sys
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

class UsBankHomePage:
	def  __init__(self, browser):
		self._browser = browser
		self._statusCode = 404
		self._authenticationFailedError = False
		self._html = requests.get(browser.current_url)
		self._soup = BeautifulSoup(self._html, 'html.parser')

	@property
	def HasAuthenticationFailedError(self):
		return self._authenticationFailedError;

	def IsValidLoginPage(self):
		try:
			self._browser.find_element_by_id('uname')
		except NoSuchElementException:
			return False
		return True

	def _checkForAuthenticationFailedError(self):
		html = requests.get(self._browser.current_url)
		homePageHtml = BeautifulSoup(html, 'html.parser')
		authenticationFailed = homePageHtml.find(text='Error 403: AuthenticationFailed')
		self._authenticationFailedError = len(authenticationFailed.contents) > 0

	def Login(self, username, password):
		_checkForAuthenticationFailedError()
		if HasAuthenticationFailedError:
			# TODO: Add error message to login result
			return False

		self._browser.find_element_by_id('uname').clear()
		self._browser.find_element_by_id('pword').clear()

		self._browser.find_element_by_id('uname').send_keys(username)
		self._browser.find_element_by_id('pword').send_keys(password)
		self._browser.find_element_by_link_text('Log In').click()

		error = self._browser.find_element(By.XPATH, '//h6[@class="error"]')
		if(len(error.contents) > 0):
			# TODO: Add error message to login result
			return False

		return True