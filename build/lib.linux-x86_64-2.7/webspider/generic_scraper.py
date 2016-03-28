#!/usr/bin/env python

'''
Generic Scraper class to download the pdfs 
from any given link
'''


import bs4, os, requests
from selenium import webdriver


class Scraper(object):
	def __init__(self,parser,pagelist,log):
		'''
		Initializes the required variables, and 
		makes the directory to store the pdfs
		if not present
		'''
		self._parser=parser
		self._pagelist=pagelist
		self._log=log
		self._count=0

		try:
			if not os.path.exists('downloaded_pdfs'):
				os.makedirs('downloaded_pdfs')
		except OSError as e:
			print('Scraper Error : while checking/making directory : ' + e)
			self._log.write('Scraper Error : while checking/making directory :  %s\n'%e)

		try:		
			self._browser=webdriver.Firefox()
		except:
			print('Scraper Error : could not open firefox browser')
			self._log.write('Scraper Error : could not open firefox browser\n')



	def _download(self,page):
		'''
		Given a page, downloads and returns 
		the source of that page
		'''
		print('downloading page %s'%page)
		self._log.write('downloading page : %s\n'%page)
		try:
			self._browser.get(page)
			html_source=self._browser.page_source
			return html_source
		except:
			print('could not download the page %s\n'%page)
			self._log.write('could not download the page %s\n'%page)



	def _store(self,pdf_url):
		'''
		Given a pdf url, downloads and stores the pdf
		in ./downloaded_pdfs folder
		'''

		self._count+=1
		print('storing pdf %s'%pdf_url)
		self._log.write('storing pdf : %s\n'%pdf_url)

		res=requests.get(pdf_url)
		
		try:
			res.raise_for_status()
		except:
			print('Scraper error : error while storing the pdf  %s'%pdf_url)
			self._log.write('Scraper error : error while storing the pdf  %s\n'%pdf_url)
			return

		if res!=None:
			pdfFile=open(os.path.join('downloaded_pdfs',os.path.basename(pdf_url)),'wb')
			for chunk in res.iter_content(1024):
				pdfFile.write(chunk)
			pdfFile.close()
		


	def run(self):
		'''
		Use all the other functions of the module to 
		download the pdfs, and works as the only public method 
		of the class.
		'''
		for page_list in self._pagelist:

			for page in page_list:

				html=self._download(page)
				pdf_url=self._parser.parse(html)
				self._store(pdf_url)

		self._browser.quit()
		log.write('\n\nNumber of pdfs downloaded : %s'%self._count)


