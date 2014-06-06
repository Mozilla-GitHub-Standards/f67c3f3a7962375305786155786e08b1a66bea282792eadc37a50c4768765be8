# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import os
from setuptools import setup, find_packages

requires = ['bottle']


setup(name='omxen',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      description='A fake SMS gateway',
      zip_safe=False,
      license='APLv2.0',
      classifiers=[
        "Programming Language :: Python",
      ],
      install_requires=requires,
      author='Mozilla Services',
      author_email='services-dev@mozilla.org',
      url='https://github.com/mozilla-services/omxen',
      entry_points="""
      [console_scripts]
      omxen = omxen:main
      """)
