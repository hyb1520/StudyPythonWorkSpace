#!/usr/bin/env python3
# -*-coding:utf-8-*-


class Student():
    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


s = Student()
s.set_score(65)
print(s.get_score())


class classmate():
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


t = classmate()
t.score = 60
print(t.score)
