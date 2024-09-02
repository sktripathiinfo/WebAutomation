import logging


class BaseClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)

        FileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        # if you give level name at run time python will see what kind of error message we are getting
        # and what kind of level it was

        FileHandler.setFormatter(formatter)

        logger.addHandler(FileHandler)
        logger.setLevel(logging.INFO)
        return logger

