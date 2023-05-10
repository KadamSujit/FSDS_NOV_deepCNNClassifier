import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s" #set logging format as per our requirement
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, # logging level
    format=logging_str, # logging format
    handlers= [ #means if we want logging statments only in file or also in terminal, here we want both
        logging.FileHandler(log_filepath), # writes o/p in file
        logging.StreamHandler(sys.stdout), #prints output in terminal
    ])

logger = logging.getLogger("deepClassifierLogger")
