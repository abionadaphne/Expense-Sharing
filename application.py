#!/usr/bin/python
import os
import sys

import logging
logging.basicConfig(stream = sys.stderr)

### This is the entry-point to the web application.

sys.path.insert(0, os.path.dirname(__file__) or '.')

PY_DIR = os.path.join(os.environ['OPENSHIFT_HOMEDIR'], "python")

virtenv = PY_DIR + '/virtenv/'

PY_CACHE = os.path.join(virtenv, 'lib', os.environ['OPENSHIFT_PYTHON_VERSION'], 'site-packages')

os.environ['PYTHON_EGG_CACHE'] = os.path.join(PY_CACHE)
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    exec(open(virtualenv).read(), dict(__file__=virtualenv))
except IOError:
    pass

from run import app as application

