#!/usr/bin/env python


def func():
    try:
        raw_input('press any key to continue...')
        exit()
        print 'in the end'
    except KeyboardInterrupt, SystemExit:
        print '\nKeyboardInterrupt or SystemExit'
    except Exception:
        print 'in the exception'


if __name__ == '__main__':
    func()
