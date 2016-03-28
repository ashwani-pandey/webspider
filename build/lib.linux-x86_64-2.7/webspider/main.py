#!/usr/bin/env python

'''
Main module to download the pdfs
'''

from selenium import webdriver
import bs4, os, sys, requests
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from datetime import datetime


from generic_scraper import *
from trai_parser import *


def get_scraper(log):
	'''
	Creates an object of Parser, and 
	passes that as argument to Scraper,
	and return an object of Scraper
	'''
	parser=Parser()
	pagelist=Pagelist(log)

	return Scraper(parser,pagelist,log)


if __name__=='__main__':
	
	if not os.path.exists('logs'):
		os.makedirs('logs')

	file_name= datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	log=open(os.path.join(os.getcwd(),'logs',file_name),'w')

	scraper=get_scraper(log)
	scraper.run()

	log.close()
