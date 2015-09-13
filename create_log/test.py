#-*-coding=utf-8-*-

import logging
import sys

'''
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
'''

###############################################################################
'''
logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s:打印日志的当前函数
%(lineno)d:打印日志的当前行号
%(asctime)s:打印日志的时间
%(thread)d:打印线程ID
%(threadName)s:打印线程名称
%(process)d:打印进程ID
%(message)s:打印日志信息
datefmt:指定时间格式，同time.strftime()
level:设置日志级别，默认为logging.WARNING
stream:指定将日志的输出流，可以指定输出到sys.stderrys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
'''
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='my.log',
                    filemode='w',
#                    stream=sys.stdout,
                    )
###############################################################################

###############################################################################
'''
将日志同时输出到文件和屏幕
定义一个StreamHandler, 将INFO级别或者更高级别的日志信息打印到标准输出，
并将其添加到当前的日志处理对象
'''
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
###############################################################################

logging.debug('This is debug')
logging.info('This is info')
logging.warning('This is warning')
