
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
            self.myclient = MongoClient("asdflocalefdsfdsfhos")
            self.mydb = self.myclient["mydatabase"]
        except:
            print("MongoDB not connected")
            
    def reconnect(self):
        connected = False
        try:
            self.myclient = MongoClient("gfglocalhodsfstsdfsdfsdasdf")
            self.mydb = self.myclient["mydatabase"]
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