

A javascript enabled spider to download all the pdf files accessible on the following link : http://trai.gov.in/Content/PressReleases.aspx  , and then to make the spider generic so that it works for any site.



MOZILLA FIREFOX is a must to run this program!

NOTE : The code has been well tested on Ubuntu 14.04 LTS, and the given procedure should work 
		perfectly for the same!


Similarly, make sure that python 2.7 and pip is already installed on your environment.



******************************************************************************************************************

AUTOMATIC SETUP to run the program ( If it fails for some reason, manual installation guidelines given below ) : 


1. Extract files from webspider-1.0.tar.gz

2. cd into webspider-1.0 and run the following command : 

		sudo python setup.py install

   #################################
   If an error comes due to the download of lxml, you can run the following command : 

		sudo apt-get install libxml2-dev libxslt1-dev python-dev

   and then run the command :

		sudo python setup.py install

   #################################


3. Type the following in your terminal to start downloading the pdfs : 

		trai_pdfs	


And hurray, the download of the pdfs will start automatically.

The logs will be saved in the logs folder, and you can also see the logs being generated on the terminal itself.

The downloaded pdfs will be presnet in downloaded_pdfs folder.

********************************************************************************************************************





MANUAL INSTALLATION GUIDELINES to run the program ( in case the automated setup fails ) : 

1. cd into webspider folder where requirements.txt file is present.

2. Make sure that virtualenv is already installed. If not, run the following command

		pip install virtualenv

3. Create a virtual environment for the project by running the following command

		virtualenv -p /usr/bin/python2.7 venv

4. Activate the virtual environment by running the following command

		source venv/bin/activate


5. Run the following command to download all the requirements: 
	
		pip install requirements.txt

6. cd into webspider folder again where the 3 python modules are present
		6.1. main.py
		6.2. generic_scraper.py
		6.3. trai_parser.py

7. Run the following command to start downloading all the pdf files from the given link

		python main.py






In the webspider folder : 

	logs folder - contains the generated logs everytime you run main.py module with the timestamp as its name

	downloaded_pdfs folder - contains all the downloaded pdfs







