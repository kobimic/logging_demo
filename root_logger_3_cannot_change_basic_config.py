import logging

# root logger to console

logging.basicConfig(level=logging.DEBUG)
logging.debug("This will get logged")

logging.basicConfig(level=logging.WARNING)
logging.debug("This will STILL get logged")
