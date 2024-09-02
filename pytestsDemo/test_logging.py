import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    FileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    # if you give level name at run time python will see what kind of error message we are getting
    # and what kind of level it was

    FileHandler.setFormatter(formatter)

    logger.addHandler(FileHandler)
    logger.setLevel(logging.INFO)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue occurred ")



# import logging
#
# def test_loggingDemo():
#     logger = logging.getLogger(__name__)
#
#     # Create a file handler
#     file_handler = logging.FileHandler("logfile.log")
#     file_handler.setLevel(logging.DEBUG)
#
#     # Create a formatter and set it for the file handler
#     formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#     file_handler.setFormatter(formatter)
#
#     # Add the file handler to the logger
#     logger.addHandler(file_handler)
#
#     # Set the logging level for the logger
#     logger.setLevel(logging.DEBUG)
#
#     # Log messages
#     logger.debug("A debug statement is executed")
#     logger.info("Information statement")
#     logger.warning("Something is in warning mode")
#     logger.error("A major error has happened")
#     logger.critical("Critical issue occurred ")
#
# # Running the test function to see logs
# test_loggingDemo()
