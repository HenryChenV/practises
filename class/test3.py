#!/usr/bin/env python

class SortKeyDict(dict):
    def keys(self):
        return sorted(super(SortKeyDict, self).keys())


if __name__ == '__main__':
    import pdb; pdb.set_trace() ### XXX BREAKPOINT
    d = SortKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))
    print 'By iterator:'.ljust(12), [key for key in d]
    print 'By keys:'.ljust(12), d.keys()
