import logging
import sys
import os
import config

class Logger:
    log = logging.getLogger("TESTING")

    def create_logs(self):
        Logger.log.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logging.getLogger('testing').addHandler(handler)
        if not os.path.exists(config.logs_path):
            os.mkdir(config.logs_path)
        filehandler = logging.FileHandler(config.logs_path + "/test.log")
        filehandler.setFormatter(formatter)
        Logger.log.addHandler(filehandler)
        Logger.log.propagate = False