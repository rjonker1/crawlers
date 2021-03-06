import time
import logging

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener

class ScreenshotCapture(AbstractEventListener):
	"""Capture Screen Shots"""
	def __init__(self, crawler):
		self._crawler = crawler
	
	def on_exception(self, exception, driver):
		logging.error(str(exception))
		screenshot_name = 'exception_%s.png' % time.strftime("%Y%m%d-%H%M%S")
		driver.save_screenshot('screenshots/%s/%s' % (self._crawler, screenshot_name))
		logging.info('Screenshot Captured as %s' % screenshot_name)