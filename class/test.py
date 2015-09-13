#!/usr/bin/env python
#-*-encoding=UTF-8-*-

class TestStaticMethod:
    sv1 = 'henry'
    def __init__(self):
        self.lv= 'lv is here'

    @staticmethod
    def foo():
        print 'calling static method foo()'
#    foo = staticmethod(foo)
#        print sv1
#        print self.lv

class TestClassMethod:
    sv1 = 'henry'
    def __init__(self):
        print self
        self.lv= 'lv is here'

    @classmethod
    def foo(cls):
        print cls
        print cls.sv1
#        print 'calling class method foo()'
#        print 'foo() is part of class:', cls.__name__
#    foo = classmethod(foo)
#        print sv1
#        print self.lv


if __name__ == '__main__':
#    tsm = TestStaticMethod()
#    TestStaticMethod.foo()
#    tsm.foo()

    scm = TestClassMethod()
    TestClassMethod.foo()
    scm.foo()
