#!/usr/bin/env python3
# -*-coding:utf-8-*-

class Student():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


s = Student('Jack')


class Fib():
    # def __init__(self):
    a, b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a


class Chain(object):
    def __init__(self, path='lll'):
        self.sspath = path
        print('4')
        print(self.sspath)

    def user(self, name='xxx'):
        self.name = name
        return Chain('%s/%s' % (self.sspath, self.name))

    def __getattr__(self, path):
        print('5')
        print(path)
        print(self.sspath)
        return Chain('%s/%s' % (self.sspath, path))

    def __str__(self):
        print('6')
        return self.sspath

    __repr__ = __str__


ch = Chain()
# .user.timeline.list

# print(ch.status.us.timeline.list)
print(ch)
