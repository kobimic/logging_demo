import logging
from file_with_child_logger import my_method

logger1 = logging.getLogger("main logger")
logger1.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger1.addHandler(handler)
logger1.info("This will NOT be logged TWICE!!!!")

my_method()

logger1.info("Program Done")