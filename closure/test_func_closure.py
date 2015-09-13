#!/usr/bin/env python

output = '<int %r id=%#0x val=%d>'
w = x = y = z = 1


def func1():
    x = y = z = 2


def func2():
    y = z = 3
    def func3():
        z = 4
        print output % ('w', id(w), w)
        print output % ('x', id(x), x)
        print output % ('y', id(y), y)
        print output % ('z', id(z), z)

    clo = func3.func_closure
    if clo:
        print 'func3 closure vars:', [str(c) for c in clo]
    else:
        print 'no func3 closure vars'
    func3()

    clo = func2.func_closure
    if clo:
        print 'func2 closure vars:', [str(c) for c in clo]
    else:
        print 'no func2 closure vars'

clo = func1.func_closure
if clo:
    print 'func1 closure vars:', [str(c) for c in clo]
else:
    print 'no func1 closure vars'
func1()
func2()
