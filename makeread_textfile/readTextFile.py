#!/usr/bin/env python

"read and display test file"

# get filename
fname = raw_input('Please input filename: ')

# read and display test file
try:
	text = open(fname, 'r')
except IOError, e:
	print 'open file failed: %s' % e
else:
	for eachline in text:
		print eachline,

print 'DONE'
