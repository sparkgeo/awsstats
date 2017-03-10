#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


import os

here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.md'))
long_description = f.read().strip()
f.close()

setup(
    name='awsstats',
    version='0.1.0',
    author='Sparkgeo',
    author_email='dustin@sparkgeo.com',
    url='https://github.com/sparkgeo/awsstats',
    description='',
    packages=find_packages(),
    long_description=long_description,
    keywords='',
    zip_safe=False,
    install_requires=[
        'boto3',
    ],
    include_package_data=True,
    classifiers=[
        'Framework :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
