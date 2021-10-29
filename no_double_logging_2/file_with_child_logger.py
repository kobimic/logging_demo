import logging

logger = logging.getLogger("another_logger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def my_method():
    logger.info("Hello from method (1)")
    logger.warning("Hello from method (2)")
