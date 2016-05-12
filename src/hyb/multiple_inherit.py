#!/usr/bin/env python3
# -*-coding:utf-8-*-

class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMinxIN(object):
    def run(self):
        print('running')


class FlyableMixIn(object):
    def fly(self):
        print('flying')


class Dog(Mammal,RunnableMinxIN):
    pass


class Bat(Mammal,RunnableMinxIN):
    pass


class Parrot(Bird,FlyableMixIn):
    pass


class Ostrich(Bird,FlyableMixIn):
    pass


d = Dog()
d.run()