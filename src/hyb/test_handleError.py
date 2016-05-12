#!/usr/bin/env python3
# -*-coding:utf-8-*-

import logging
import pdb

logging.basicConfig(level=logging.DEBUG)

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    logging.debug('exxxxx')
    print('except:', e)
finally:
    pass


s = '0'
n= int(s)
pdb.set_trace()
print(10/n)