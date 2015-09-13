#!/usr/bin/env python

class P1:
    def foo(self):
        print 'called P1-foo()'

class P2:
    def foo(self):
        print 'called P2-foo()'

    def bar(self):
        print 'called P2-bar()'

class C1(P1, P2):
    pass

class C2(P1, P2):
    def bar(self):
        print 'called C2-bar()'

class GS(C1, C2):
    pass


if __name__ == '__main__':
    gs = GS()
    gs.foo()
    gs.bar()
