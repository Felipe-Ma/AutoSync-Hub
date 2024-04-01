# logger_config.py
import logging

def setup_logger():
    # Create a logger
    logger = logging.getLogger('webhook_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    handler = logging.FileHandler('webhook.log')
    handler.setLevel(logging.DEBUG)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger