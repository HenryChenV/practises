#!/usr/bin/python


def testexcpt():
    try:
        print "return 'A' * 10"
        1 / 0
        return 'A' * 10
    except:
        print "return 'B' * 10"
        return 'A' * 10
    finally:
        print "return 'C' * 10"
        return 'C' * 10


if __name__ == '__main__':
    print testexcpt()
