class Father(object):

    def __init__(self):
        print 'initialized Father'

    def __del__(self):
        print 'delete Father'

class Child(Father):

    def __init__(self):
        print 'initialized Child'

    def __del__(self):
        Father.__del__(self)
        print 'delete Child'


c1 = Child()
c2 = c1
c3 = c2

print id(c1), id(c2), id(c3)
import ipdb; ipdb.set_trace() ### XXX BREAKPOINT

