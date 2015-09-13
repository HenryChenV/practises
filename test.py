# coding=utf-8
v = 1.0


def foo():
    global v
    v += 1.0
    print v

#foo()


aa = raw_input('number: ')
print type(aa), aa
