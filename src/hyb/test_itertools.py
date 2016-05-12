#!/usr/bin/env python3
# -*-coding:utf-8-*-

import itertools

natuals = itertools.count(1)

cs = itertools.cycle('ABC')

ns = itertools.repeat('M', 10)

items = itertools.takewhile(lambda x: x < 10, natuals)
print(list(items))


for c in itertools.chain('ABC','XYZ'):
    print(c)

