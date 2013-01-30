#!/usr/bin/env python
from distutils.core import setup

setup(
    name='sugercube',
    version='1.0.0',
    description='Sugercube is the main ingredient for making scoail-able py.',
    author='Muntasir Mohiuddin',
    author_email='muntasir.mohiuddin@gmail.com',
    url='https://github.com/mmohiudd/sugercube',
    license='Apache',
    packages=['sugercube'],
    long_description=open("README.md").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
    install_requires=[
        'requests>=1.1.0',
    ],
)
