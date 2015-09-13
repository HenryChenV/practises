#!/usr/bin/env python

'''
'''

from urllib import urlretrieve


def firstNonBlankLine(lines):
    for line in lines:
        if line:
            return line


def fistLast(webpage):
    with open(webpage) as fp:
        lines = fp.readlines()
    print 'First NonBlank Line:\n', firstNonBlankLine(lines)
    lines.reverse()
    print 'Last NonBlank Line:\n', firstNonBlankLine(lines)


def download(url='http://localhost'):
    try:
        retval = urlretrieve(url)[0]
        if retval:
            fistLast(retval)
    except IOError, e:
        print e


if __name__ == '__main__':
    download()
