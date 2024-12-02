import math
import logging

# Configure logging (log to console by default)
logging.basicConfig(level=logging.DEBUG, \
                     format='%(asctime)s - %(levelname)s - %(message)s')

# different log levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


try:
    100 / 0  
except ZeroDivisionError as e:  
    logging.error(f"Error: {e}")
