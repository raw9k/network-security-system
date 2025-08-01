import os, sys, json

from dotenv import load_dotenv  # type: ignore
load_dotenv()

import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import pymongo # type: ignore



MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def cv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    file_path = "Network_data\phisingData.csv"
    database = "ROUNAK_KUMAR"
    collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json(file_path = file_path)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records=records, database= database,collection=collection)
    print(no_of_records)
    