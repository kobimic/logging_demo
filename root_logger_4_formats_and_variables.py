# import logging
#
# logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.info("this will start the file...")
# logging.warning("This will get logged to a file")


import logging

logging.basicConfig(format='%(levelname)-7s | %(asctime)-10s | %(message)s', level=logging.INFO)
logging.info("this will start the file...")
logging.warning("This will get logged to a file")

name = "kobi"
logging.info(f"Hello log from {name}")

logging.info("Hello log from %s", name)

logging.info({"name": "kobi"})

import json

dict_name = {"name1": "kobi1"}
logging.info(json.dumps(dict_name))
