#!/usr/bin/python

"this is a test module"

def hello():
    print 'hello, world!'

def change(mylist):
    mylist[0] = 3
    mylist[1] = 9


def newfoo(x, y, *arg_list, **arg_dict):
    print x, y
    print arg_list
    print arg_dict


if __name__ == '__main__':
#    newfoo(1, 2, 3, 4, ['h', 'e'], key='name', value='me')
