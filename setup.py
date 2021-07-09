# -*- coding: utf-8 -*-

import BloodDroplet

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.txt'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(this_directory, 'CHANGELOG.txt'), encoding='utf-8') as f:
    changes = f.read()

required = ['numpy', 'opencv']

setup(
    name='Blood-Droplet',
    version=BloodDroplet.__version__,
    packages=['BloodDroplet'],
    author='Krishna Kadam',
    author_email='krisskad0@gmail.com',
    maintainer='Krishna kadam',
    url="https://github.com/krisskad/BloodDroplet",
    description='Image Processing, Preprocessing Module, Extract Blood Droplet, Masking Image',
    long_description=readme + '\n\n' + changes,
    long_description_content_type='text/x-rst',
    license='MIT License',
    requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ]
)
