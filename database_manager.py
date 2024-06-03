from constant import MONGODB_URL,DATABASE_NAME
from datetime import timedelta
from pymongo import MongoClient

class mongodb:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    
    def __init__(self):
        try:
            self.myclient = MongoClient(MONGODB_URL)
            self.mydb = self.myclient[DATABASE_NAME]
        except:
            print("MongoDB not connected")
            
    def reconnect(self):
        connected = False
        try:
            self.myclient = MongoClient(MONGODB_URL)
            self.mydb = self.myclient[DATABASE_NAME]
            connected = True
        except:
            print("MongoDB not connected")
        return connected

    # enter values in database
    def enter(self, name, data):
        self.mycollection = self.mydb[name]
        self.mycollection.insert_one(data)
        
    def print_(self):
        # print("hell0")
        return False