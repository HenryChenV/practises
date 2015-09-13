#coding:utf-8
import logging
# 创建一个logger
logger = logging.getLogger('henry')
logger.setLevel(logging.INFO)
logger2 = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log', 'w')

fh2 = logging.FileHandler('test2.log', 'w')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
#logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)
logger2.addHandler(fh2)
logger2.addHandler(ch)

# 记录一条日志
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')
