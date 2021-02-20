#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='PyTadoLog',
      version='0.1.0',
      description='CSV logger for PyTado from Josh Gibson',
      long_description=long_description,
      keywords='tado',
      author='Josh Gibson',
      author_email='josh-gibson@outlook.com',
      url='https://github.com/lpforthewin/TadoLogger',
      python_requires='>=3.6',
      install_requires=[
        'keyring',
        'numpy',
        'openpyxl',
        'pandas',
        # Get PyTado from GitHub because PyPi version doesn't work with Python3
        'python-tado @ git+https://git@github.com/chrism0dwk/PyTado.git'
      ],
      license="MIT",
      platforms=["any"],
      packages=find_packages(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Home Automation',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
      ],
      scripts=['scripts/csv2excel'],
      zip_safe=False,
)
