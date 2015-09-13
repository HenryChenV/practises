#!/usr/bin/env python

'''
'''


def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval


def main():
    'handle all the data processing'
    log = open('carddata.log', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError:
        ccfile.close()
        log.write('no txns this month.\n')
        return

    txns = ccfile.readlines()
    ccfile.close()

    total = 0.00
    log.write('account log:\n')
    for line in txns:
        result = safe_float(line)
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')
        else:
            log.write('ignored: %s' % (result))
    print '$%.2f (new balance)' % (total)
    log.close()


if __name__ == '__main__':
    main()
