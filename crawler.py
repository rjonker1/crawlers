import sys
import logging
import logging.config

from us_bank.us_bank_private_crawler import UsBankPrivateCrawler

def _crawl():	
	usBankPrivateCrawler = UsBankPrivateCrawler()
	usBankPrivateCrawler.Crawl()

def _setupLogger():
	logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
	datefmt='%m-%d %H:%M',
	filename='logs/crawler.log',
	filemode='w')

	console = logging.StreamHandler()
	console.setLevel(logging.INFO)
	# set a format which is simpler for console use
	formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
	# tell the handler to use this format
	console.setFormatter(formatter)
	# add the handler to the root logger
	logging.getLogger('').addHandler(console)

def main():
	_setupLogger()
	_crawl()
	logging.info('Crawl Ended')

if __name__ == '__main__':
	main()