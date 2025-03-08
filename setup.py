#!/usr/bin/env python

# Standard library imports
from os import path
from pathlib import Path

# 3rd party imports
from setuptools import setup, find_packages

# Setting useful paths
this_directory = path.abspath(path.dirname(__file__))
config_dir = this_directory / Path("HalApyJson") / Path("CONFIG")

# Reading the contents of your README file
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Reading the contents of your requirements file
with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = f.read().strip().split('\n')

# This setup is suitable for "python setup.py develop".

setup(name ='HalApyJson',
      version ='1.1.3',
      description ='Python modules for parsing the response to a HAL API request',
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      include_package_data = True,
      license = 'MIT',
      classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research'
        ],
      entry_points = {
        'console_scripts': ['cli_hal = HalApyJson.CLI.cli:cli_hal',],
        },
      keywords = 'Metadata parsing, HAL request, API management',
      install_requires = install_requires,
      author = 'BiblioAnalysis team',
      author_email = 'francois.bertin7@wanadoo.fr, amal.chabli@orange.fr',
      url = 'https://github.com/Bertin-fap/HalApyJson',
      packages = find_packages(),
      )
