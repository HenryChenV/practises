#!/usr/bin/env python
#-*- coding=utf-8 -*-


class TestSetAndGet(object):
    def __init__(self):
        self.kv = {}

    def __getitem__(self, key):
        return self.kv[key]

    def __setitem__(self, key, value):
        self.kv[key] = value

    def __pfunc(self):
        print 'private func'


if __name__ == '__main__':
    a = TestSetAndGet()
    a['first'] = 1
    print a['first']
    a.__setitem__('second', 2)
    print a.__getitem__('second')
    print a['second']

#    a.__pfunc()
