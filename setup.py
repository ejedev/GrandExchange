import setuptools
from distutils.core import setup
setup(
  name = 'GrandExchange',
  packages = ['GrandExchange'],
  version = '0.1',
  license='GPL-3.0',
  description = 'A python wrapper for OSBuddy exchange data.',
  author = 'ejedev',
  author_email = 'ev3098@gmail.com',
  url = 'https://github.com/ejedev/GrandExchange',
  download_url = 'https://github.com/ejedev/GrandExchange/archive/v0.1.tar.gz',
  keywords = ['OSRS', 'Oldschool','Runescape','Grand','Exchange','OSBuddy'],
  install_requires=[
    'wheel',
          ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
