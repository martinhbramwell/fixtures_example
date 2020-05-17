# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in example_app/__init__.py
from example_app import __version__ as version

setup(
	name='example_app',
	version=version,
	description='Show how Frappe "export-fixtures" works',
	author='M. Bramwell',
	author_email='https://github.com/martinhbramwell/fixtures_example',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
