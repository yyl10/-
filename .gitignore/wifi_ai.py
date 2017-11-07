#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2017 lyy 
import authenticate
import os
import sys
import ShutdownWifi
from datetime import datetime
import get_is_internet

def main(argv):

	# make a copy of original stdout route
#	stdout_backup = sys.stdout	#输出导向原始地址
	log_file = open("log.log", "a")#	a 是追加，w 只写  r 只读
	sys.stdout = log_file
	print '\n'
	print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print '\n'
	print argv
	if argv[1]=='shut':
		if get_is_internet.is_on_internet()==0:
			ShutdownWifi.login_account_shut_wifi()
	else:
		if argv[1]=='login':
			if get_is_internet.is_on_internet()!=0:
				authenticate.login_accounts()
#	sys.stdout = stdout_backup	#还原输出到屏幕
	log_file.close()

if __name__ == '__main__':
#	import sys
#	sys.exit(main(sys.argv))
	main(sys.argv)
