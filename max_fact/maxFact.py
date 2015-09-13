#!/usr/bin/env python
#-*-encoding=utf-8-*-

'''
todo
'''


def showmaxFactor(num):
    count = num >> 1
    while count > 1:
        if 0 == num % count:
            print 'The max factor of %s is %s.' % (num, count)
            break
        count -= 1
    else:
        print num, 'is prime.'


if __name__ == '__main__':
    for eachNum in xrange(10, 27):
        showmaxFactor(eachNum)
