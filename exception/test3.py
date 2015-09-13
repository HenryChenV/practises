#!/usr/bin/env python


class MyException(Exception('My fault.')):
    pass


def func():
    try:
        raise Exception('hello, everybody.')
    except Exception, e:
        print e


if __name__ == '__main__':
    func()
