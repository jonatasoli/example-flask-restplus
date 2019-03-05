import logging
import os
from logging.handlers import RotatingFileHandler


def create_logger(app):
    level = logging.INFO if app.config.get("DEBUG") else logging.ERROR
    format = "------------------------------------------------\n%(levelname)s %(asctime)s %(filename)s:%(lineno)s | %(funcName)s() %(name)s %(message)s"

    logging.basicConfig(filename=(os.path.join(app.config.get("BASEDIR"), "logs", "partyou.log")), level=level,
                        format=format, datefmt='%d/%m/%Y %H:%M:%S')

    logger = logging.getLogger('partyou_logger')

    handler = RotatingFileHandler(filename=(os.path.join(app.config.get("BASEDIR"), "logs", "partyou.log.old")),
                                  maxBytes=50000000, backupCount=20)  # 50MB
    logger.addHandler(handler)

    app.plogger = logger
    return app
