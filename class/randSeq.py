#!/usr/bin/env python

from random import choice

class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return choice(self.data)


if __name__ == '__main__':
    rs = RandSeq(range(10))
    for i in range(10):
        print rs.next()
