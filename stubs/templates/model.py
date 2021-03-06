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

from #APPNAME.ext.paginate import will_paginate

class #MODELCLASS(BaseModel):
    db_conn = DBConn()
    db = db_conn.get_db()
    collection_name = "#MODEL_COLLECTION"
    collection = db[collection_name]
    def __init__(self, *args, data={}, schema={}, **kwargs):
        #super(#MODELCLASS, self).__init__(data)
        """ Basic instance setup"""
        #super(#MODELCLASS,self).__init__(*args, **kwargs)
        #print("created a new #MODELCLASS, id:", id(self))
        #self.collection_name = "#MODEL_COLLECTION"
        self.modelname = "#MODELNAME"
        self.modelname_plural = powlib.pluralize(self.modelname)
        #self._db_conn = DBConn()
        #self.db = self._db_conn.get_db()
        #self.collection = self.db[self.collection_name]
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
            self.set_values(data)

    # example for extension use
    # @will_paginate(per_page=10)
    # also look at the import above
    def find(self, *args, sort=False, **kwargs):
        return super(#MODELCLASS,self).find(*args,**kwargs)
