# import logging
#
# # root logger to console
#
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This will get logged")


# # root logger to file
#
# import logging
#
# logging.basicConfig(filename='app.log', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.info("this will start the file...")
# logging.warning("This will get logged to a file")
#


# root logger to file NEW each time

import logging

logging.basicConfig(filename='app.log',filemode="w", format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info("this will start the file...")
logging.warning("This will get logged to a file")