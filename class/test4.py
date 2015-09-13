#!/usr/bin/env python

class A(object):
    __var1 = 1

    def __init__(self):
        self.__var2 = 2

    def __foo(self):
        pass

class __B(object):
    pass

class _C(object):
    pass
