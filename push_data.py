import os, sys, json

from dotenv import load_dotenv
import pandas as pd
import numpy as np
import pymongo

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__():
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def cv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    