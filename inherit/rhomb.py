#!/usr/bin/env python

class A:
    def __init__(self):
        print '__init__() in A'

class B(A):
    pass

class C(A):
    def __init__(self):
        print '__init__() in C'

class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
