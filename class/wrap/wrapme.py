class WrapMe(object):

    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
#        return 'self.__data'

    def __getattr__(self, attr):
        return getattr(self.__data, attr)


if __name__ == '__main__':
    wrappedComplex = WrapMe(3.14+15.9j)
    print wrappedComplex
    print str(wrappedComplex)
    print repr(wrappedComplex)
    print wrappedComplex.real
    print wrappedComplex.imag
    print wrappedComplex.conjugate()
    print wrappedComplex.get()
    print dir(wrappedComplex)
