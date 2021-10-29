# # 1
# import logging
#
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.critical("this is critical")


# # 2
# import logging
#
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This will get logged")

# #3
# import logging
#
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# logger.info("This will NOT get logged, even after setting the level to info!!!")
# logger.warning("This WILL get logged 1")


#4
import logging

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("This WILL get logged 1")
logger.warning("This WILL get logged 2")