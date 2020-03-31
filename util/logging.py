import logging
import sys


__log = None


def get_custom_logger(name, log_level=logging.DEBUG):
    global __log

    if __log is None:
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        # handler = logging.FileHandler('/var/log/feeder_urbanite.log', mode='w')
        # handler.setFormatter(formatter)
        screen_handler = logging.StreamHandler(stream=sys.stdout)
        screen_handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        # logger.addHandler(handler)
        logger.addHandler(screen_handler)
        __log = logger

    return __log
