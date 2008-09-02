#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8

import re
from setuptools import setup, find_packages
import tracext.adsense

setup(name=tracext.adsense.__package__,
      version=tracext.adsense.__version__,
      author=tracext.adsense.__author__,
      author_email=tracext.adsense.__email__,
      url=tracext.adsense.__url__,
      download_url='http://python.org/pypi/%s' % tracext.adsense.__package__,
      description=tracext.adsense.__summary__,
      long_description=re.sub(r'(\.\.[\s]*[\w]*::[\s]*[\w+]*\n)+', r'::\n',
                              open('README.txt').read()),
      license=tracext.adsense.__license__,
      platforms="OS Independent - Anywhere Python, Trac >=0.11 is known to run.",
      install_requires = ['Trac>=0.11'],
      keywords = "adsense trac",
      packages=['tracext', 'tracext.adsense'],
      namespace_packages=['tracext'],
      classifiers   = ['Framework :: Trac'],
      entry_points = """
      [trac.plugins]
        tracext.adsense = tracext.adsense
        tracext.adsense.ads = tracext.adsense.ads
        tracext.adsense.admin = tracext.adsense.admin
        tracext.adsense.config = tracext.adsense.config
        tracext.adsense.search = tracext.adsense.search
      """
)
