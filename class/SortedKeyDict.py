class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


d = SortedKeyDict((('henry-chen', 66), ('conke-hy', 77), ('sandy-zhou', 88)))
print type(d), d
print 'By Iterator: '.ljust(1), [k for k in d]
print 'By keys()  : '.ljust(12), d.keys()
