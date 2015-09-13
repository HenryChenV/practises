#!/usr/bin/env python
#-*-encoding=utf-8-*-


queue = []


def enQ():
    queue.append(raw_input('Please enter new string: ').strip())


def deQ():
    if 0 == len(queue):
        print 'Cannot Dequeue from a empty queue!'
    else:
        print 'Remove [%s]' % repr(queue.pop(0))


def viewQ():
    print queue


CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}


def showmenu():
    pr = '''
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: '''

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            if choice not in 'edvq':
                print 'Invalid option: [%s], try again.'
            else:
                break

        if choice == 'q':
            print 'Bye!'
            break

        CMDs[choice]()


if __name__ == '__main__':
    showmenu()
