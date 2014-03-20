#
#
# This file was autogenerated by PythonOnWheels (copow version)
# But YOU CAN EDIT THIS FILE SAFELY
# It will not be overwritten by python_on_wheels
# unless you force it with the -f or --force option
# 
# 2013/06/19 13:30:31


import sys
import os

import copow.lib.powlib
from copow.lib.pow_objects import Migration
from models.app import App

migration = Migration()

def up(self):
    """ up method will be executed when running do_migrate -d up"""
    app = App( schema  = {
            "oid"            :      { "type" : "Text" },
            "name"               :      { "type" : "Text" },   
            "path"               :      { "type" : "Text" },
            "lastversion"        :      { "type" : "Text" },
            "currentversion"     :      { "type" : "Text" }
            #"a_more_complex_one"    :       { "type" : "Text" , "index" : True, "default" : "something"}
        } 
    )

    # creates the tabke (collection) and the schema in migrations/schemas/
    migration.create_table(app)
    
    
def down(self):
    """ down method will be executed when running do_migrate -d down"""
    # drops the table (collection) and removes the schema from migrations/schemas/
    app = App()
    migration.drop_table(app)
    
    
