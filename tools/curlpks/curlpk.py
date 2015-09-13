#!/usr/bin/env python

import os
from urllib import urlretrieve
from shutil import copyfile
import threading


lock_stdout = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        lockPrint('%s start.' % self.name)
        self.func(*self.args)
        lockPrint('%s done.' % self.name)


def lockPrint(s):
    if lock_stdout.acquire():
        print s
        lock_stdout.release()


def getpks(filename):
    pks = []
    with open(filename) as fp:
        pks = [line.strip() for line in fp]
    return pks


def curlpk(pks):
    dirroot = '/var/www/html/openstack-icehouse/'
    urlroot = 'https://repos.fedorapeople.org/repos/openstack/openstack-icehouse/epel-6/'
    for pk in pks:
        if not os.path.exists(dirroot + pk):
            # lockPrint('[%s]' % pk)
            if not os.path.exists(pk):
                lockPrint('Downloading %s...' % (pk))
                urlretrieve(urlroot + pk, pk)
                # os.system('curl -# -O %s%s' % (urlroot, pk))
            if not os.path.exists(dirroot + pk):
                lockPrint('%s -> %s%s' % (pk, dirroot, pk))
                copyfile(pk, dirroot + pk)
                # os.system('sudo cp -v %s %s%s' % (pk, dirroot, pk))


def curlstatus():
    dirroot = '/var/www/html/openstack-icehouse/'
    pks = []
    pks = getpks('package2')
    pks_len = len(pks)
    pks_gp_len = len(pks) / 10
    pks_gps = [pks[i: i + pks_gp_len] for i in xrange(0, pks_len, pks_gp_len)]
    downedpks = os.listdir(dirroot)
    i = 0
    for pks_gp in pks_gps:
        if set(pks_gp) < set(downedpks):
            print 'group%d done!' % i
        i += 1


def main():
    if os.getuid() != 0:
        print 'pls run as root !'
        exit()

    pks = []
    pks = getpks('package2')
    pks_len = len(pks)
    pks_gp_len = len(pks) / 10
    pks_gps = [pks[i: i + pks_gp_len] for i in xrange(0, pks_len, pks_gp_len)]

    mythreads = []
    i = 0
    for pks_gp in pks_gps:
        t = MyThread(func=curlpk, args=(pks_gp,), name='group%d' % i)
        mythreads.append(t)
        i += 1
    for t in mythreads:
        t.start()
    for t in mythreads:
        t.join()

    # curlpk(pks[:10])


if __name__ == '__main__':
    main()
