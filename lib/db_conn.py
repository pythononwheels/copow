#
#
# MongoDB Connection
#
#
from pymongo import MongoClient
#from #APPNAME.config import dbconfig
import importlib

class DBConn(object):
    
    # class variables
    num_instances = 0

    def __init__(self, env="development"):
        """
            imports the right configuration for the environment env.
            Default environment is development.
        """
        mod = importlib.import_module("#APPNAME.config.db" )        
        dbconf = mod.__dict__[env]
        self.client = MongoClient(dbconf["host"], dbconf["port"]  )
        #DBConn.connection = pymongo.Connection()
        self.db = self.client[dbconf["database"]]
        DBConn.num_instances += 1

    def get_client(self):
        return self.client

    def get_db(self):
        return self.db
    
    def get_num_instances(self):
        return self.num_instances



