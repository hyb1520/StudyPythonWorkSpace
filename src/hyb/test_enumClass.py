#!/usr/bin/env python3
# -*-coding:utf-8-*-

from enum import Enum, unique

Week = Enum('Week', ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sta', 'Sun'))
for name, member in Week.__members__.items():
    print(name, '=>', member, ',', member.value)
Enum.


@unique
class Car(Enum):
    Bmw = 0
    Bens = 1
    Auto = 2

car1 = Car.Bmw
print(car1.value)
print(Car(1))
