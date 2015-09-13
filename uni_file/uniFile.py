#!/usr/bin/env python

'''
An example of reading and writing Unicode strings:
Writes an Unicode string to a file in utf-8 and read it back in.
'''

def main():
    CODEC = 'utf-8'
    FILE = 'unicode.txt'

    hello_out = u'hello, world!'
    bytes_out = hello_out.encode(CODEC)
    fp = open(FILE, 'w')
    fp.write(bytes_out)
    fp.close()

    fp = open(FILE, 'r')
    bytes_in = fp.read()
    fp.close()
    hello_in = bytes_in.decode(CODEC)
    print hello_in,

if __name__ == '__main__':
    main()
