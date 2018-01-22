import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler



logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s {%(pathname)s:%(lineno)d} %(message)s')
handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=10)
handler.setFormatter(formatter)
logger.addHandler(handler)


class LogLevel:
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class TraceException:
    def __init__(self, ex_str):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        self.message = '{}:{}-{}:{}'.format(fname, exc_tb.tb_lineno, exc_type, ex_str)
        # print(exc_type, fname, exc_tb.tb_lineno)

    def get_message(self):
        return self.message


    def write_log(self):
        logger.log(LogLevel.ERROR, self.message)


    def __str__(self):
        return self.message

# def getLogger():
#     logger = logging.getLogger('simple_logger')
#     logger.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.DEBUG)
#     ch.setFormatter(formatter)
#     logger.addHandler(ch)
#     return logger
