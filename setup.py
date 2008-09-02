#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8

import re
from setuptools import setup, find_packages
import tracext.google.search

setup(name=tracext.google.search.__package__,
      version=tracext.google.search.__version__,
      author=tracext.google.search.__author__,
      author_email=tracext.google.search.__email__,
      url=tracext.google.search.__url__,
      download_url='http://python.org/pypi/%s' % tracext.google.search.__package__,
      description=tracext.google.search.__summary__,
      long_description=re.sub(r'(\.\.[\s]*[\w]*::[\s]*[\w+]*\n)+', r'::\n',
                              open('README.txt').read()),
      license=tracext.google.search.__license__,
      platforms="OS Independent - Anywhere Python, Trac >=0.11 is known to run.",
      install_requires = ['Trac>=0.11'],
      keywords = "adsense trac",
      packages=['tracext', 'tracext.google', 'tracext.google.search'],
      namespace_packages=['tracext', 'tracext.google'],
      classifiers   = ['Framework :: Trac'],
      entry_points = """
      [trac.plugins]
        tracext.google.search = tracext.google.search
        tracext.google.search.admin = tracext.google.search.admin
        tracext.google.search.search = tracext.google.search.search
      """
)
