#
#
# Model #MODELCLASS
# automatically created: #DATE by copow
# 
#

from #APPNAME.lib.db_conn import DBConn
from #APPNAME.migrations.schemas.#MODEL_SCHEMA_schema import #MODEL_SCHEMA as schema
#from #APPNAME.models.basemodels.base#MODELNAME import Base#MODELCLASS
from #APPNAME.models.basemodels.base import BaseModel
#import #APPNAME.lib.powlib
from #APPNAME.lib import powlib

class #MODELCLASS(BaseModel):
    
    def __init__(self, data=None, schema={}):
        #super(#MODELCLASS, self).__init__(data)
        """ Basic instance setup"""
        self.collection_name = "#MODEL_COLLECTION"
        self.modelname = "#MODELNAME"
        self.modelname_plural = powlib.pluralize(self.modelname)
        self._db_conn = DBConn()
        self.db = self._db_conn.get_db()
        self.collection = self.db[self.collection_name]
        #self.related_models = {}
        if schema:
            self.schema = schema
            if "#MODELNAME_relations" in schema.keys():
                self.relations = schema["#MODELNAME_relations"]
            else:
                self.relations = {}
        else:
            self.load_schema()
        self.setup_properties()
        #print self.schema
        #print dir(self)
        if data:
            self.set_data(data)


