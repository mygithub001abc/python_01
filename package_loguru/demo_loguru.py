# loguru模块
"""
功能
1.可以格式化日志
2.着色（以不同的颜色显示）
3.生成到文件
4.显示不同的日志级别
5.只使用一个对象（非常方便）
"""

# 1.下载安装：pip install loguru  /显示 pip show loguru  升级 python -m pip install --upgrade pip


# 2.导包
from loguru import logger

# 3.打印一条日志

logger.info('hello world!')

# 输出不同的日志级别，分别是debug, info, warning, success, error
logger.debug('这是一条debug日志')  # 调试日志
logger.info('这是一条info日志')  # 普通日志
logger.warning('这是一条warning日志')  # 警告日志
logger.success('这是一条success日志')  # 成功日志
logger.error('这是一条error日志')  # 错误日志
#
# # 将日志输出到文件 add()
# 时间格式化 format='{time:YYYY-MM-DD HH:mm:ss}'
logger.add('a.log', format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {line} | {message}', level='DEBUG')
logger.debug('这是一条debug日志')  # 调试日志
logger.info('这是一条info日志')  # 普通日志
logger.warning('这是一条warning日志')  # 警告日志
logger.success('这是一条success日志')  # 成功日志
logger.error('这是一条error日志')  # 错误日志

# 进行传入参数的格式化
logger.info('我的名字是{},我今年{}了', '武则天', 18)
logger.info('我的名字是{},我今年{}了'.format('武则天', 18))

# 日志文件保存（了解）
"""
logger.add("file_1.log", rotation="500 MB") # 文件过大就会重新生成一个文件
logger.add("file_2.log", rotation="12:00") # 每天12点创建新文件
logger.add("file_3.log", rotation="1 week") # 文件时间过长就会创建新文件
logger.add("file_X.log", retention="10 days") # 一段时间后会清空
logger.add("file_Y.log", compression="zip") # 保存zip格式
"""

