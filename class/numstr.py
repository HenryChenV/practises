#!/usr/bin/env python

class PNumStr(object):

    def __init__(self):
        print 'init PNumStr'
        self.__test = 'just for test'

class NumStr(PNumStr):
    def __init__(self, num=0, string=''):
        print 'init %s' % self.__class__.__name__
        super(self.__class__, self).__init__()
        self.__num = num
        self.__string = string

    def __str__(self):
        print 'in __str__'
        print self._NumStr__num
        print self._PNumStr__test
        return '[%d :: %r]' % (self.__num, self.__string)
    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.__num + other.__num, self.__string + other.__string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __mul__(self, count):
        if isinstance(count, int):
            return self.__class__(self.__num * count, self.__string * count)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return self.__norm_cval(cmp(self.__num, other.__num)) + \
                    self.__norm_cval(cmp(self.__string, other.__string))
        else:
            raise TypeError, 'Illegal argument type for built-in operation'


if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string='boo')
    f = NumStr(1)
    print str(a)
