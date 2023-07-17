import sys
from loguru import logger

# doc_link = "https://loguru.readthedocs.io/en/stable/api/logger.html"

def init_logger(log_file='default_{time:YYYY-MM-DD}.log', level='DEBUG', pid=False, tid=False, ):
    pid_str = ' pid:{process}' if pid else ''
    tid_str = ' tid:{thread}' if tid else ''

    # remove the default console logger sink and re-add it
    logger.remove(handler_id=None)
    logger.add(
        sink=sys.stdout,
        level=level,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> |<cyan>%s</cyan><cyan>%s</cyan> <cyan>{name}</cyan>:<cyan>{function}</cyan> @ <cyan>{file}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"%(pid_str, tid_str)
    )

    # log to file
    logger.add(
        sink=log_file,
        level=level,
        encoding="utf-8",
        enqueue=True,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level: <8}</level> |%s%s {name}:{function} at {file}:{line} - {message}"%(pid_str, tid_str)
    )


def test_log():
    logger.debug('This is debug information, level 10')
    logger.info('This is info information, level 20')
    logger.success('This is success information, level 25')
    logger.warning('This is warn information, level 30')
    try:
        1/0
    except:
        logger.exception('This is exception information, level 40')


if __name__ == '__main__':
    init_logger()
    test_log()
    logger.error('This is error information, level 40')
    logger.critical('This is critical information, level 50')