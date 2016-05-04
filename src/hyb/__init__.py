#!/usr/bin/env python3
# -*-coding:utf-8-*-
from functools import reduce


def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


def power(x, n=2):
    s = 1
    for mun in range(n):
        s = s * x
    return s


def calc(*numbers):
    s = 0
    for n in numbers:
        s = s + power(n)
    return s


def f1(a, b, c=0, *args, **kwargs):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kwargs=', kwargs)


def f2(a, b, c=0, *, d, **kwargs):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kwargs=', kwargs)


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def move(n, a, b, c):
    if n == 1:
        print(a, "->", c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


def fib(n):
    i = 0
    a = 0
    b = 1
    while i < n - 1:
        atmp = a
        a = b
        b = atmp + b
        i = i + 1
    return b


def normalize(name):
    return str(name).capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))


def prod(L):
    def pd(x, y):
        return x * y

    return reduce(pd, L)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def is_palindrome(n):
    if n >= 100:
        x = n // 100
        tmp = n % 100
        y = tmp // 10
        z = tmp % 10
        if n == z * 100 + y * 10 + x:
            return True
        else:
            return False
    elif n >= 10:
        x = n // 10
        y = n % 10
        if n == y * 10 + x:
            return n
        else:
            return False
    else:
        return False


output = filter(is_palindrome, range(1, 1000))
print(list(output))
