#!/usr/bin/env python
#-*-encoding=utf-8-*-

'''
把列表作为堆栈用于存储和取回输入的字符串
'''

stack = []


def pushit():
    stack.append(raw_input('Enter New String: ').strip())


def popit():
    if len(stack) == 0:
        print 'Cannot pop from a empty stack!'
    else:
        print 'Remove [', repr(stack.pop()), '].'


def viewstack():
    print stack

CMDs = {'u': pushit, 'o': popit, 'v': viewstack}


def showmenu():
    pr = '''
=======================================
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit

Enter your choice: '''

    while True:
        try:
            choice = raw_input(pr).strip()[0].lower()
        except (EOFError, KeyboardInterrupt, IndexError):
            choice = 'q'
        print '\nYou picked: [%s]' % choice
        if choice not in 'uovq':
            print 'Invalid option: %s, try again' % choice
        elif 'q' == choice:
            print 'Bye!'
            break
        else:
            CMDs[choice]()

if __name__ == '__main__':
    showmenu()
