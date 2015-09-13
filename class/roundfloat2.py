#!/usr/vin/env python

class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), 'Value must be a Float!'
        self.value = round(val, 2)

    def __str__(self):
        return str('%.2f' % self.value)

    __repr__ = __str__


if __name__ == '__main__':
    rfm = RoundFloatManual(3.1415)
    import pdb; pdb.set_trace() ### XXX BREAKPOINT

