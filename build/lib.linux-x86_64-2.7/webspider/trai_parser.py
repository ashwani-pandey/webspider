#!/usr/bin/env python

'''
This module is specific for the link
of the TRAI given in the beginning
'''


import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class Parser(object):
	def parse(self,html):
		'''
		Takes html as input, and
		returns the url of pdf
		'''
		pdf_soup=bs4.BeautifulSoup(html,"lxml")
		pdf_tags=pdf_soup.select('.news_content_mid a')
		pdf_data='http://trai.gov.in/'+pdf_tags[0].get('href')
		return pdf_data




def Pagelist(log):
	'''
	A generator that yields a list of pages
	that contains the urls of the pdfs to be 
	downloaded.	
	'''

	try:
		browser=webdriver.Firefox()
		browser.get('http://trai.gov.in/Content/PressReleases.aspx')
	except:
		print('Pagelist function error : error with opening of browser')
		log.write('Pagelist function error : error with opening of browser\n')

	# html for the first page
	html_source=browser.page_source
	soup=bs4.BeautifulSoup(html_source,"lxml")
	nextTags=soup.select('#ctl00_ContentPlaceHolder1_lbtnNext')
	last=nextTags[0].get('disabled')

	# condition to check whether the last page has been reached or not
	while last==None:

		page_list=[]
		pressTags=soup.select('.upcoming a')
		for i in range(len(pressTags)):
			page_list.append('http://trai.gov.in'+pressTags[i].get('href'))
			#print page_list[-1]

		yield page_list

		try:
			linkElem=browser.find_element_by_id('ctl00_ContentPlaceHolder1_lbtnNext')
			linkElem.click()
		except:
			print('Pagelist function error : error while clicking the Next button')
			log.write('Pagelist function error : error while clicking the Next button\n')

		html_source=browser.page_source
		soup=bs4.BeautifulSoup(html_source,"lxml")
		nextTags=soup.select('#ctl00_ContentPlaceHolder1_lbtnNext')
		last=nextTags[0].get('disabled')





if __name__=='__main__':
	'''
	Checks if the Pagelist function is working properly,
	and this won't run when this module is imported
	'''

	magic_pages=pagelist()

	for page_list in magic_pages:
		print len(page_list)
		print 'done!'



