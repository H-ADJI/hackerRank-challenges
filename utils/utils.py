'''
File: utils.py
File Created: Saturday, 14th January 2023 6:59:31 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
import re
import time
import os
from pathlib import Path
CHALLENGES_PATH = "./challenges"
FILES_NAME_PATTERN = r".+(?=\.py)"
challenge_files = os.listdir(CHALLENGES_PATH)


def get_challenge_name(file_name: str):
    return re.search(pattern=FILES_NAME_PATTERN, string=file_name).group()


def get_file_creation_date(file_name: str):
    return os.path.getctime(Path(CHALLENGES_PATH).joinpath(file_name))
