#!/usr/bin/env python

class A:
    def __init__(self):
        print '__init__() in A'

class B(object):
    pass

class C(object):
    def __init__(self):
        print '__init__() in C'

class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
