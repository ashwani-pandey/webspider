

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requires=[
    'beautifulsoup4==4.4.1',
    
    'lxml==3.6.0',
    'nose==1.3.7',
    'requests==2.9.1',
    'selenium==2.53.1',
    'wheel==0.24.0'
    ]


config = {
    'description': 'webspider',
    'author': 'Ashwani Pandey',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ashwani.pnd@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['webspider'],
    'scripts': [],
    'name': 'webspider',
    'install_requires': requires,

    'entry_points':{
        "console_scripts": [
                "trai_pdfs = webspider.main:main"
            ]
    }
}

setup(**config)