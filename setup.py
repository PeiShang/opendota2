#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script"""
from setuptools import setup

setup(
    name="opendota2",
    version="0.1.1",
    author="PeiShang",
    author_email="shangpei92@foxmail.com",
    url="https://github.com/PeiShang/opendota2",
    description="The OpenDota web API in Python",
    license="GPL",
    keywords="dota2 dota api dota2api opendota",
    packages=['opendota2', 'opendota2.src', 'opendota2.ref'],
    package_data={'opendota2.ref': ['abilities.json',
                                   'heroes.json',
                                   'leaver.json',
                                   'items.json',
                                   'lobbies.json',
                                   'modes.json',
                                   'regions.json']},
    install_requires=['pandas'],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ]
    )
