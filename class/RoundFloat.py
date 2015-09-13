#-*-coding=utf-8-*-

class RoundFload(float):
    def __new__(cls, val):
        print '1', cls
        print '2', cls.__class__
        print '3', RoundFload
        print '4', super(RoundFload, cls)
        return super(cls, cls).__new__(cls, round(val, 2))
#        return super(RoundFload, cls).__new__(cls, round(val, 2))


class NormalClass(object):

    def __init__(self):
        print 'init'
        print self

    def __new__(self):
        print 'new'
        print self
        return self


rf = RoundFload(3.14159)
#print rf
#print NormalClass()
