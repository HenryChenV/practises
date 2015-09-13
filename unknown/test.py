a = range(1000)
s = set(a)
d = dict((i, 1) for i in a)
%timeit -n 10000 in d
%timeit -n 10000 in s
