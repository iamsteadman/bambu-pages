#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
    name = 'bambu-pages',
    version = '2.0',
    description = 'Tools for Django webapps',
    author = 'Steadman',
    author_email = 'mark@steadman.io',
    url = 'https://github.com/iamsteadman/bambu-pages',
    long_description = open(path.join(path.dirname(__file__), 'README')).read(),
    install_requires = [
        'Django>=1.4',
        'bambu-attachments',
        'bambu-markup',
        'bambu-formatrules'
    ],
    packages = [
        'bambu_pages',
        'bambu_pages.migrations'
    ],
    package_data = {
        'bambu_pages': [
            'templates/pages/*.html',
            'templates/search/indexes/pages/*.txt'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django'
    ]
)
