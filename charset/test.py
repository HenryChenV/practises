#-*-coding=utf-8-*-

u = u'汉'
print u # u'\u6c49'
print repr(u) # u'\u6c49'

s = u.encode('UTF-8')
print s
print repr(s) # '\xe6\xb1\x89'

u2 = s.decode('UTF-8')
print u2
print repr(u2) # u'\u6c49'

# 对unicode进行解码是错误的
# s2 = u.decode('UTF-8')
# 同样，对str进行编码也是错误的
# u2 = s.encode('UTF-8')
