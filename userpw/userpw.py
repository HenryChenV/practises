#!/usr/bin/env python
#-*-encoding=utf-8-*-

'''
'''

db = {}


def newuser():
    prompt = 'login desired: '
    while True:
        login = raw_input(prompt)
        if login in db:
            prompt = 'login is already existed, try again: '
        else:
            break

    pwd = raw_input('new password: ')
    db[login] = pwd
    print 'Saved.'


def olduser():
    login = raw_input('login: ')
    if login not in db:
        print 'login does not exist.'
    else:
        pwd = raw_input('password: ')
        if pwd == db[login]:
            print 'Welcome back', login
        else:
            print 'Password Incorrectly.'


def showmenu():
    prompt = '''
    (N)ew user
    (O)ld user
    (Q)uit
Enter your choice: '''

    quit = False
    while not quit:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked [%s]' % choice
            if choice not in 'noq':
                print 'Invalid option, try again.'
            else:
                chosen = True

        if 'q' == choice:
            quit = True
        elif 'n' == choice:
            newuser()
        elif 'o' == choice:
            olduser()
        print


if __name__ == '__main__':
    showmenu()
