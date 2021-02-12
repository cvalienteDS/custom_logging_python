import logging
import logging.config
from Utils.setup_logging import setup_logging

if __name__ == '__main__':
    os.makedirs("log", exist_ok=True)
    setup_logging("Utils/logging.yaml")
    logger = logging.getLogger(__name__)
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.exception("This is an exception message")
