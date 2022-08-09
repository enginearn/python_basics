#!/usr/bin/env python3

import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.FileHandler("logtest.log")
logger.addHandler(h)

def do_something():
    logger.debug('Doing something from logtest.py')
    logger.debug('Done something from logtest.py')


if __name__ == '__main__':
    sys.exit(0)

