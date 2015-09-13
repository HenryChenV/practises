class SlottedClass(object):
#    __slots__ = ('version', 'bar')
    __slots__ = ()

    def foo():
        print "I'm foo"


class TestClass(object):
    pass
