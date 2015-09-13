class P(object):
    Pversion = 2.2

    def __init__(self):
        print 'haha, P is here'
        self.Pbalabala = 'fine day'


class C(P):
    pass


print dir(C)
print
c = C()
print dir(c)
