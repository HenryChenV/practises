#!/usr/bin/env python

'''
'''

from time import ctime, sleep


def decofunc(func):
    def wrappedFunc():
        print '[%s] called %s' % (ctime(), func.__name__)
        return func()
    return wrappedFunc

@decofunc
def foo():
    print 'this is foo'


if __name__ == '__main__':
    for i in xrange(3):
        foo()
        sleep(3)
