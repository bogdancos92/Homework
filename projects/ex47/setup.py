try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project Swordfish',
    'author': 'Costea Bogdan',
    'url': 'http://www.google.com',
    'download_url': 'http://www.google.com',
    'author_email': 'bogdancos92@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)