#!/usr/bin/env python

from operator import add, sub
from random import randint, choice


MAXTRIED = 2
ops = {'+': add, '-': sub}

def doprob():
    op = choice('+-')
    nums = [randint(0, 9) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)

    oops = 0
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'Correctly !'
                break
            else:
                print 'Incorrectly !'
                oops += 1
                if oops >= MAXTRIED:
                    print pr, ans
                    break
        except (EOFError, KeyboardInterrupt):
            print
            break
        except (ValueError):
            print 'Invalid input... Try again.'
    print


def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again?[y]')
        except (EOFError, KeyboardInterrupt):
            opt = 'n'
        if opt and opt[0] == 'n':
            break

if __name__ == '__main__':
    main()
