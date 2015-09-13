#!/usr/bin/env python
#-*-encoding=utf8-*-

'''
据说这是黑客写的阶乘,能杜绝安全漏洞
'''

import sys


def fact(x, acc=1):
    if x: return fact(x.__sub__(1), acc.__mul__(x))
    return acc


if __name__ == '__main__':
    sys.stdout.write(str(fact(6)) + '\n')
