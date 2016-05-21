#!/usr/bin/env python

import os
from glob import glob

from setuptools import setup


setup(
    name='carbon',
    version='0.9.15.1',
    url='http://graphite-project.github.com',
    author='Chris Davis',
    author_email='chrismd@gmail.com',
    license='Apache Software License 2.0',
    description='Backend data caching and persistence daemon for Graphite',
    packages=['carbon', 'carbon.aggregator', 'twisted.plugins'],
    package_dir={'' : 'lib'},
    package_data={'carbon' : ['*.xml']},
    scripts=glob('bin/*'),
    install_requires=['twisted==16.1.1', 'whisper'],
    extras_require={'amqp': ['txamqp']}
)
