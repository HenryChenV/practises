#!/usr/bin/env python


gg = 'xyz'


def foo():
    print 'gg in foo():', gg
    print 'id(gg) in foo():', id(gg)
    global gg
    gg = 'abc'
    print 'gg in foo():', gg
    print 'id(gg) in foo():', id(gg)



if __name__ == '__main__':
    print 'id(gg):', id(gg)
    foo()
