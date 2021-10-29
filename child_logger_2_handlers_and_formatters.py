#1
import logging

logger = logging.getLogger("example_logger")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("This is a info, and the default level is still info BUT it is also info for the handler!!!")


logger.setLevel(logging.WARNING)
logger.info("this is info...")
logger.warning("this is warning...")


