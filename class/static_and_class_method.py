#-*- coding=utf-8 -*-

class TestStaticMethod(object):

    def __init__(self):
        self.bar = 33.3

    @staticmethod
    def foo():
        print 'static methood'


class TestClassMethod(object):
    ver = 22.2

    @classmethod
    def foo(cls):
        print cls
        print 'class method'
        print cls.ver


if __name__ == '__main__':
    TestStaticMethod.foo()
    TestClassMethod.foo()
