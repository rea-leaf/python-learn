from Logger import Logger
from Log import Log
log = Logger('all-11.log',level='debug')
log.logger.debug('debug')
log.logger.info('info')
log.logger.warning('警告')
log.logger.error('报错')
log.logger.critical('严重')
log2 = Log.get_logger()
log = Log.get_logger()
log2.info('test')
log.info('test')