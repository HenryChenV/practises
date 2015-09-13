#-*- coding=utf-8 -*-

from time import time, ctime


class TimedWrapMe(object):
    '''
    会记录obj的创建时间（ctime），修改时间（mtime）和访问时间（atime）
    '''

    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError, "argument of 'c', 'm' or 'a' required"
        attr = '_%s__%stime' % (self.__class__.__name__, t_type[0])
        print attr
        return getattr(self, attr)

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return 'self.__data'

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        print 'in func __getattr__'
#        attr = '_%s_ctime' % (self.__class__.__name__)
#        print hasattr(self, attr)
        self.__atime = time()
        return getattr(self.__data, attr)


if __name__ == '__main__':
    twm = TimedWrapMe('henry')
    print twm.gettimeval('c')
