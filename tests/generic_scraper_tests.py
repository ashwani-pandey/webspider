
from nose.tools import *
from webspider.generic_scraper import Scraper
from webspider.trai_parser import Parser

def test_scraper_construct():

	test_parser=Parser()
	test_file_obj=open('tests/test_file.txt','w')
	test_scraper=Scraper(test_parser,[],test_file_obj)

	assert isinstance(test_scraper._parser,Parser)
	assert_equal(test_scraper._pagelist,[])
	assert isinstance(test_scraper._log,file)
	assert_equal(test_scraper._count,0)

	test_file_obj.close()



def test_scraper_run_empty():

	test_parser=Parser()
	test_file_obj=open('tests/test_file.txt','w')
	test_scraper=Scraper(test_parser,[],test_file_obj)

	test_scraper.run()

	test_file_obj.close()



def test_scraper_run_nonempty():

	test_parser=Parser()
	test_file_obj=open('tests/test_file.txt','w')
	test_pagelist=[['http://trai.gov.in/Content/PressDetails/52324_0.aspx','http://trai.gov.in/Content/PressDetails/52325_0.aspx'],
					['http://trai.gov.in/Content/PressDetails/52322_0.aspx']
				]

	test_scraper=Scraper(test_parser,test_pagelist,test_file_obj)

	test_scraper.run()

	test_file_obj.close()


