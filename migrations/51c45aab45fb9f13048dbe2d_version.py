#
#
# This file was autogenerated by PythonOnWheels (copow version)
# But YOU CAN EDIT THIS FILE SAFELY
# It will not be overwritten by python_on_wheels
# unless you force it with the -f or --force option
# 
# 2013/06/21 15:52:43


import sys
import os

import #APPNAME.lib.powlib
from #APPNAME.lib.pow_objects import Migration
from #APPNAME.models.version import Version

migration = Migration()

def up():
      """ up method will be executed when running do_migrate -d up"""
    version = Version( schema  = {
            "short_name"     :      { "type" : "Text" },   
            "long_name"      :      { "type" : "Text" },
            "path"           :      { "type" : "Text" },
            "comment"        :      { "type" : "Text" }
            #"a_more_complex_one"    :       { "type" : "Text" , "index" : True, "default" : "something"}
        } 
    )

    # creates the tabke (collection) and the schema in migrations/schemas/
    migration.create_table(version)
    
    
def down():
    """ down method will be executed when running do_migrate -d down"""
    # drops the table (collection) and removes the schema from migrations/schemas/
    version = Version()
    migration.drop_table(version)
    
    
