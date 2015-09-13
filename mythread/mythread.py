#!/usr/bin/env python

import threading


lock_out = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)
        if lock_out.acquire():
            print self.name, 'done.'
            lock_out.release()


def hello(sth1, sth2):
    if lock_out.acquire():
        print 'hello', sth1, sth2
        lock_out.release()


def main():
    c = 4
    threads = []

    for i in xrange(c):
        t = MyThread(func=hello, args=('aa', 'bb'), name='group%d' % i)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
