#!/usr/bin/env python

'''
'''


def convert(func, numseq):
    return [func(num) for num in numseq]


if __name__ == '__main__':
    myseq = (123, 45.67, -6.2e8, 999999999L)
    print myseq
    for func in (int, long, float):
        print convert(func, myseq)
