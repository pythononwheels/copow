#
#
# This file was autogenerated by PythonOnWheels (copow version)
# But YOU CAN EDIT THIS FILE SAFELY
# It will not be overwritten by python_on_wheels
# unless you force it with the -f or --force option
# 
# #DATE


import sys
import os

import #APPNAME.lib.powlib
from #APPNAME.lib.pow_objects import Migration
from #APPNAME.models.#MODELNAME import #UP_MODELNAME

migration = Migration()

def up(self):
    """ up method will be executed when running do_migrate -d up"""
    #MODELNAME = #UP_MODELNAME( schema  = {
           #"title"      :      { "type" : "Text" },   
           #"author"     :      { "type" : "Text" },
           #"content"    :      { "type" : "Text" }
           #"a_more_complex_one"    :       { "type" : "Text" , "index" : True, "default" : "something"}
      } 
    )

    # creates the tabke (collection) and the schema in migrations/schemas/
    migration.create_table(#MODELNAME)
    
    
def down(self):
    """ down method will be executed when running do_migrate -d down"""
    # drops the table (collection) and removes the schema from migrations/schemas/
    #MODELNAME = #UP_MODELNAME()
    migration.drop_table(#MODELNAME)
    
    
