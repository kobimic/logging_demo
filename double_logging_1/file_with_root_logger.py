import logging

# logging.info("this is info, but it will NOT print")
#
#
# def my_method():
#     logging.info("from method 1")
#     logging.warning("from method 2")


logger2 = logging.getLogger()
logger2.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s WTF!!!!!")
handler.setFormatter(formatter)
logger2.addHandler(handler)

def my_method():
    logger2.info("Hello from method (1)")
    logger2.warning("Hello from method (2)")