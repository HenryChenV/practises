#!/usr/bin/env python

def displayNumType(num):
	print num, 'is',

	if isinstance(num, (int, long, float, complex)):
		print 'a number of type: ', type(num).__name__
	else:
		print 'not a number at all !!!'

displayNumType(69)
displayNumType(69L)
displayNumType(11.1)
displayNumType(5 + 4j)
displayNumType('xxx')
