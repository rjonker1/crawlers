import sys
import platform

if platform.system() == 'Windows':
	PHANTOMJS_PATH = './phantomjs.exe'
else:
	PHANTOMJS_PATH = './phantomjs'