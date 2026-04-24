import os
import sys
import json
import certifi
import pymongo
import numpy as np
import pandas as pd

from dotenv import load_dotenv
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException   


load_dotenv()
MONGO_DB_URL = os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

ca = certifi.where()

class NetworkSecurityExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(inplace=True,drop=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def push_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == '__main__':
    try:
        FILE_PATH = "Network_Data\phisingData.csv"
        DATABASE = "BEEBASSI_DB"
        COLLECTION = "NetworkData"

        networkobject = NetworkSecurityExtract()
        records = networkobject.csv_to_json_converter(file_path=FILE_PATH)
        print(records)

        no_of_records = networkobject.push_data_to_mongodb(records,DATABASE,COLLECTION)
        print(f"Number of records pushed to MongoDB: {no_of_records}")
    except Exception as e:
        raise NetworkSecurityException(e,sys)