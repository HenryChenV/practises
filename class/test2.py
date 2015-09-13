#!/usr/bin/env python

class A(object):

    def __init__(self):
        print 'I am A %s' % self.__class__

    def foo(self):
        print 'Hi, I am A-foo()'

class B(object):

    def __init__(self):
        print 'I am B %s' % self.__class__

    def foo(self):
        print 'Hi, I am B-foo()'

class C(A, B):
    def foo(self):
        super(C, self).foo()
        print 'Hi, I am C-foo()'

if __name__ == '__main__':
#    a = A()
#    a.foo()
#    print

#    b = B()
#    b.foo()
#    print

    c = C()
    c.foo()
    print
