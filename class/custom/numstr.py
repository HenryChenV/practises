#!/usr/bin/env python
#-*- coding=utf-8 -*-

def _foo():
    pass

def bar():
    pass

class NumStr(object):

    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[%d::%s]' % (self.__num, self.__string)

    __repr__ = __str__

    def __check_argument_type(self, argument, type):
        if not isinstance(argument, type):
            raise TypeError, \
                    'Illegal argument type for build-in operation.'

    def __add__(self, other):
        self.__check_argument_type(other, self.__class__)
        return self.__class__(self.__num + other.__num, \
                              self.__string + other.__string)

    def __mul__(self, num):
        self.__check_argument_type(num, int)
        return self.__class__(self.__num * num, self.__string * num)

    def __nonzero__(self):
        if self.__num == 0 and self.__string == '':
            return False
        return True

    def __norm_cval(self, cmpress):
        return cmp(cmpress, 0)

    def __cmp__(self, other):
        print '***************', other.__num
        self.__check_argument_type(other, self.__class__)
        return self.__norm_cval(cmp(self.__num, other.__num)) \
                + self.__norm_cval(cmp(self.__string, other.__string))


if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string='boo')
    f = NumStr(1)
    print a
    print b
    print c
    print d
    print e
    print f
    print a < b
    print b < c
    print a == a
    print b * 2
    print a * 3
    print b + e
    print e + b
    if d: print 'not false'
    if e: print 'not false'
    print cmp(a, b)
    print cmp(a, c)
    print cmp(a, a)
    print bool(d)
    print a._NumStr__num
