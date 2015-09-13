#!/usr/bin/env python
#-*-encoding=utf8-*-

'''This is used to check identifier!
标识符合法性检查，首先要以字母或下划线开始，后面要跟字母，下划线或者数字。这里只检查长度大于2的标志符。'''

import string
import keyword

alphas = string.letters + '_'
nums = string.digits


def idcheck(id):
    if len(id) > 2:
        if id[0] not in alphas:
            print '''invalid: first symbol must be alphabetic'''
        elif keyword.iskeyword(id):
            print ''''%s' is a keyword.''' % id
        else:
            alphasnums = alphas + nums
            for eachChar in id[1:]:
                if eachChar not in alphasnums:
                    print '''invalid: remaining symbol must be alphasnumeric'''
                    break
            else:
                print '''okay as a identifier!'''
    else:
        print 'The length of identifier must longer than 2'

if __name__ == '__main__':
    print 'Welcome to the Identifier Checker v1.0.'
    print 'Testees must be at least 2 chars long.'
    myInput = raw_input('Identifier to test?')
    idcheck(myInput)
