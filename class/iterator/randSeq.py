#!/usr/bin/env python
#-*- coding=utf-8 -*-

from random import choice

class RandSeq(object):

    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        print 'in __iter__'
        return self

    def next(self):
        print 'in next'
        return choice(self.data)


if __name__ == '__main__':
    rs = RandSeq(['henry', 'tina', 'conke'])
#    iterrs = iter(rs)
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    for i in rs:
        import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
        print i
