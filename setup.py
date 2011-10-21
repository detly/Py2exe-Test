#!/usr/bin/env python
from distutils.core import setup
import py2exe

setup(
    name = 'p2etest',
    description = 'Py2exe Test',
    version = '1.0',

    console = ['app.py'],

    options = {
                  'py2exe': {
                      'packages': '',
                      'includes': '',
                  }
              },
)