# -*- coding: utf-8 -*
"""日志工具类

author: Jill

usage：
    from common.logger import Log
    log = Log().get_logger()
    log.error("error occurred when xxx")
"""
import logging
import time
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log:
    @staticmethod
    def get_logger():
        fmt = logging.Formatter('[%(asctime)s] [%(threadName)s] [%(levelname)s] [%(pathname)s:%(lineno)s]: %(message)s',
                                "%Y-%m-%d %H:%M:%S")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(fmt)
        log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        file_handler = logging.FileHandler(log_name, 'a', encoding='utf-8')  # 这个是python3的
        file_handler.setFormatter(fmt)
        logger = logging.getLogger('App')
        logger.setLevel(logging.DEBUG)
        if logger.handlers:
            return logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger


if __name__ == "__main__":
    log2 = Log.get_logger()
    log = Log.get_logger()
    log2.info('test')
    log.info('test')
    log2.error('test')
    log.warning('test')
    log.debug('test')