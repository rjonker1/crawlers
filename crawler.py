import sys

from us_bank.us_bank_private_crawler import UsBankPrivateCrawler

def crawl():
	print('Crawling US Bank')
	usBankPrivateCrawler = UsBankPrivateCrawler()
	usBankPrivateCrawler.Crawl()

if __name__ == '__main__':
	crawl()