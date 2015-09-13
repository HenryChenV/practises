#!/usr/bin/env python
#-*- coding=utf-8 -*-

'''
格式化的两种写法
'''

#print 'name: %(name)s, id: %(id)d.' % ({'id': '10', 'name': 'henry'})
print 'name: %(name)s, id: %(id)d.' % ({'id': 10, 'name': 'henry'})
print

print 'name: {name}, id: {id}.'.format(id='10', name='henry')
print 'name: {name}, id: {id}.'.format(id=10, name='henry')
print
