import logging
class Logger:
    log = logging.getLogger("TESTING")

    def create_logs(self):
        Logger.log.setLevel(logging.DEBUG)