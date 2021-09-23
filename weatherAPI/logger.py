import logging

logging.basicConfig(filename='weatherapilogs.log', filemode='a+',
                    format="%(asctime)s -%(levelname)s -%(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info("***** WELCOME TO WEATHER API LOGS *****")


class LoggingClass():
    def __init__(self):
        pass

    def logwriter(self, message):
        """This method will log the  info message in  weatherapilogs.log"""
        self.message = message
        logger.info(self.message)

    def logerror(self, message):
        """This method  will log the error message in  weatherapilogs.log"""
        self.message = message
        logger.error(self.message)