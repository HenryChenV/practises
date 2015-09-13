#!/usr/bin/env python

from time import time


def testit(func, *nkwargs, **kwargs):
    try:
        stime = time()
        retval = func(*nkwargs, **kwargs)
        dtime = time() - stime
        result = (True, retval, dtime)
    except Exception, diag:
        result = (False, str(diag), 0)
    return result


def test():
    funcs = {int, long, float}
    values = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '-' * 15, 'Function:', eachFunc.__name__, '-' * 15
        for eachValues in values:
            retval = testit(eachFunc, eachValues)
            if retval[0]:
                print '%s(%s) = ' \
                        % (eachFunc.__name__, eachValues), retval[1], \
                        'within %fus.' % ((retval[2] * 10**6))
            else:
                print '%s(%s) FAILED: ' % (eachFunc.__name__, eachValues), retval[1]


if __name__ == '__main__':
    test()
