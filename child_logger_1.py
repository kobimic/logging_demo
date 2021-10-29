# # 1
# import logging
#
# logger = logging.getLogger("example_logger")
# logger.warning("This is a warning, and the default level is still warning")
#
# logger.setLevel(logging.INFO)
# logger.info("this is info...")

# 2
import logging

logger = logging.getLogger("example_logger")
logger.setLevel(logging.INFO)
logger.info("This is a info, and the default level is still warning")
