#!/usr/bin/env python3
# -*-coding:utf-8-*-

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('L')
print(q)

defaultdd = defaultdict(lambda: 'N/A')
defaultdd['key1'] = 'abc'
print(defaultdd['key1'])
print(defaultdd['key2'])

dd = dict([('a', 1), ('b', 2), ('c', 3)])
print(dd)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:'(key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


c = Counter()
for ch in 'programing':
    c[ch] = c[ch] + 1
print(c)
