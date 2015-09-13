#!/usr/bin/env python

from time import time


def logged(when):
    def log(f, args, kwargs):
        print '''Called:
Function: %s
args: %r
kwargs: %r''' % (f, args, kwargs)

    def pre_logged(f):
        def wrapper(*args, **kwargs):
            log(f, args, args)
            return f(*args, **kwargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kwargs):
            now = time()
            try:
                return f(*args, **kwargs)
            finally:
                log(f, args, kwargs)
                print 'time delta: %fs' % (time() - now)
        return wrapper

    try:
        return {'pre': pre_logged, 'post': post_logged}[when]
    except KeyError, e:
        ValueError(e), 'must be "pre" or "post" !'


@logged('post')
def hello(name):
    print 'hello', name


if __name__ == '__main__':
    hello('dark night')
