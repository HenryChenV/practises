#!/usr/bin/env python
#-*-encoding=utf-8-*-

from itertools import product, permutations


def cal24(ns):
    e = '(({0}{4}{1}){5}{2}){6}{3}'
    nums = permutations(ns)
    ops = product('+-*/', repeat=3)
    return [e.format(*(num + op)) for num in nums for op in ops
            if eval(e.format(*(num + op))) == 24]


if __name__ == '__main__':
    print cal24([4, 6, 1, 1])
