#!/usr/bin/env python
#-*- coding=utf-8 -*-

class AnyIter(object):

    def __init__(self, seq, safe=False):
        self.safe = safe
        self.iter_seq = iter(seq)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for i in range(howmany):
            try:
                retval.append(self.iter_seq.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

if __name__ == '__main__':
    ai = AnyIter(range(10))
    print ai.next(5)
    print ai.next(5)
    print ai.next(5)
