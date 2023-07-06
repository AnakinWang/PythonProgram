from logModule.log import Log

logger = Log.getLogger("task")

def printLog():
    logger.error("logger.error")
    logger.info('logger.info')
    logger.warn('logger.warn')
    logger.warning('logger.warning')
    logger.critical('logger.critical')

if __name__ == "__main__":
    printLog()