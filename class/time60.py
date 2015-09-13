#!/user/bin/env python
#-*- coding=utf-8 -*-

class Time60(object):

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.__format_time()

    def __format_time(self):
        if self.minute >= 60:
            self.hour += self.minute / 60
            self.minute %= 60
        if self.hour >=24:
            self.hour %= 24

    def __str__(self):
        return '%d:%d' % (self.hour, self.minute)

    __repr__ = __str__

    def __add__(self, other):
        return self.__class__(self.hour + other.hour, self.minute + other.minute)

    def __iadd__(self, other):
        self.hour += other.hour
        self.minute += other.minute
        self.__format_time()
        return self


if __name__ == '__main__':
    t1 = Time60(11, 78)
    t2 = Time60(22, 89)
    print t1, t2
    t3 = t1 + t2
    print t1, id(t1), t2, id(t2), t3, id(t3)
    t1 += t2
    print t1, id(t1), t2, id(t2)
