import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        FORMAT = "[%(asctime)s :%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
       # formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        formatter = logging.Formatter(FORMAT)
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
