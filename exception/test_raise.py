#-*- coding: utf-8 -*-
#!/usr/bin/env python


def test():
    """
    测试看看return和raise的时候,会不会执行finally中的内容
    """
    try:
        a = 1 / 0
        print a
    except Exception, e:
#        return  # return依然会先执行finally
        raise e  # raise依然会先执行finally
        print 'continue run'
    finally:
        print 'finally'
        # 如果finally里面报错了,就不会执行finally里面的raise了
#        raise Exception('raise in finally')

if __name__ == '__main__':
    test()
