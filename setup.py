
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='blackini',
    version='0.1.2',
    python_requires='==3.*,>=3.6.0',
    author='Pablo Woolvett',
    author_email='pablowoolvett@gmail.com',
    entry_points={'console_scripts': ['black = blackini.__main__:main']},
    packages=['blackini'],
    package_data={},
    install_requires=['black'],
)