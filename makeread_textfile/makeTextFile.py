#!/usr/bin/env python

"To create a text file by inputed filename"

import os
ls = os.linesep

# get filename
fname = ''
while True:
    fname = raw_input('Please input the file name: ')
    if not fname:
        continue
    elif os.path.exists(fname):
        print 'ERROR: %s is already existed!' % fname
    else:
        break

# get test content
print "\nEnter lines ('.' by itself to quit).\n)"

all = []
while True:
    entry = raw_input('>')
    if '.' == entry:
        break
    else:
        all.append(entry)

# save text to file
fp = open(fname, 'w')
fp.writelines(['%s%s' % (x, ls) for x in all])
fp.close()

print 'DONE'
