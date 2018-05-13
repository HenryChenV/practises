class Parent(object):
    '''
    test getattribute
    '''

    ver = 1.0
    __foo = 'hello'

    def func_foo(self):
        return "I'm func_foo"

    def __getattr__(self, attr):
        print 'unknow attribute', attr

    def __getattribute__(self, attr):
        print 'I am __getattribute__', attr
#        return object.__getattribute__(self, attr)
        return super(type(self), self).__getattribute__(attr)
#        return self.__getattr__(attr)

    def __call__(self):
        print getattr(self, '__doc__')


p = Parent()

#print p.ver
#p.func_foo()
#p.hahaha
#p()

print p.__foo
print p._Parent__foo
print getattr(p, '_' + p.__class__.__name__ + '__foo')
