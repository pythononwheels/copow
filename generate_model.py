#!python
#  pow model generator.
#
# options are: 
#    see python generate_model.py --help

from optparse import OptionParser
import sqlite3, sys, os, datetime
import string
import sys

from copow.lib import powlib
from  copow.config import config 

APPNAME = "#APPNAME"
def main():
    """ Executes the render methods to generate a model, 
    basemodel and basic tests according to the given options """
    
    parser = OptionParser()
    
    parser.add_option( "-n", "--name",  
                       action="store", 
                       type="string", 
                       dest="name", 
                       help="""creates model named model-name.
                        You can also give a whitespace separated list. 
                       """, 
                       default ="None")

    parser.add_option( "-f", "--force",
                       action="store_true",
                       dest="force",
                       help="forces overrides of existing files",
                       default=False)

    parser.add_option( "-p", "--path",
                       action="store",
                       dest="path",
                       help="set model output path.",
                       default="./models/")
    
    (options, args) = parser.parse_args()
    
    if options.name == "None":
       if len(args) > 0:
           # if no option flag (like -n) is given, it is assumed that the 
           # first argument is the model name. (representing -n arg1)
           options.name = args
       else:
           parser.error("You must at least specify an appname by giving -n <name>.")

    model_dir = os.path.normpath(options.path)
    parts_dir = config.base["parts_dir"]
    modelname = options.name
    start = None
    end = None
    
    print(options)
    #print "options.name:  ", options.name
    
    for modelname in options.name:
        start = datetime.datetime.now()
        render_model(modelname, options.force, parts_dir, model_dir)
        end = datetime.datetime.now()
        duration = None
        duration = end - start 
        print("generated_model(s) in("+ str(duration) +")")
        print("")
        start = None
        end = None
    return

    
def render_model(modelname="NONE_GIVEN", force=False, parts_dir=config.base["parts_dir"], 
                 output_path="./models/", properties=[], comment=""):
    """
    Renders the generated Model Class in path/models.
    Renders the according BaseModel in path/models/basemodels.
    Renders a basic test in tests dierctory.
    Uses the stubs from stubs/partials.
    """
    print("generate_model: " + modelname)
    # new model filename
   

    collection_name = powlib.pluralize(modelname)
    classname = str.capitalize(modelname)  
    baseclassname = "Base" + classname

    filename = os.path.normpath(os.path.join(output_path, modelname +".py"))
    #print "filename: %s" % (filename)
    if os.path.isfile( os.path.normpath( filename ) ) and force != True:
        print(filename + " (exists)...(Use -f to force override)")
    else:
        infile = None
        infile = open (os.path.normpath( parts_dir +  "model.py"), "r")
        ostr = ""
        ostr = ostr + infile.read()
        infile.close()    

        d = datetime.datetime.now()
        ostr = ostr.replace("#DATE", d.strftime("%Y/%m/%d %H:%M:%S") )
        
        ostr = ostr.replace("#MODELCLASS", classname)
        ostr = ostr.replace("#MODEL_COLLECTION", collection_name)
        ostr = ostr.replace("#MODEL_SCHEMA", modelname)
        ostr = ostr.replace("#MODELNAME" , modelname )
        #ostr = ostr.replace("#BASECLASS", baseclassname)
        #ostr = ostr.replace("#MODELTABLE",  powlib.plural(string.lower(modelname))  ) 
        
        # write the output file to disk
        ofile = open( filename , "w+") 
        print(" --", filename + " (created)")
        ofile.write( ostr )
        ofile.close()
    
    ### generate BaseModel if neccessary
    
    filename = os.path.normpath(os.path.join(output_path + "/basemodels/", "base" + modelname +".py"))
    #print "filename: %s" % (filename)
    if os.path.isfile( filename ) and force != True:
        print(filename + " (exists)...(Use -f to force override)")
    else:
        infile = None
        ### generate the BaseClass
        infile = open (os.path.normpath( os.path.join(parts_dir +  "basemodel.py")), "r")
        ostr = infile.read()
        infile.close()
        # Add Class declaration and Table relation for sqlalchemy
        ostr = ostr.replace("#BASECLASSNAME",  baseclassname )
        ostr = ostr.replace("#MODELTABLE",  powlib.plural(str.lower(modelname))  ) 
        ostr = ostr.replace("#MODELCLASS", classname)
        ostr = ostr.replace("#MODEL_COLLECTION", collection_name)
        ostr = ostr.replace("#MODEL_SCHEMA", modelname)
        ostr = ostr.replace("#DATE", d.strftime("%Y/%m/%d %H:%M:%S") )
        ### adding the properties list
        # TODO: Needs to be tested. 
        if properties == []:
            ostr = ostr.replace("#PROPERTIES_LIST",  "[]")
        else:
            ostr = ostr.replace("#PROPERTIES_LIST",  str(properties) )

        ostr = ostr.replace("#MODELNAME" , modelname )
        
        ofile = open(  filename , "w+") 
        print(" --", filename + " (created)")
        ofile.write( ostr )
        ofile.close()
        
    # render a basic testcase 
    render_test_stub(modelname, classname, parts_dir)
    #render_schema(modelname)
    return 

def reset_model(modelname):
    """ overwrites the generated Model, BaseModel and 
    Test with empty / newly generated versions."""
    return render_model(modelname, True, "", properties=None, nomig=True)

def render_test_stub (modelname, classname, PARTS_DIR = config.base["parts_dir"] ):
    """ renders the basic testcase for a PoW Model """
    #print "rendering Testcase for:", classname, " ", " ", modelname
    print(" -- generating TestCase...", end=' ')
    d = datetime.datetime.now()
    
    infile = open( os.path.normpath( PARTS_DIR +  "test_model.py"), "r")
    test_name = "test" + modelname + ".py"
    ofile = open( os.path.normpath( config.base["model_test_dir"] + test_name ), "w")
    ostr = infile.read()
    ostr = ostr.replace("#CLASSNAME", "Test" +  classname )
    ostr = ostr.replace("#DATE", d.strftime("%Y/%m/%d %H:%M:%S") )
    ofile.write(ostr)
    infile.close()
    ofile.close()
    print(" %s...(created)" % (config.base["model_test_dir"] + test_name))
    
    return

def render_schema(modelname):
    print(" -- generating schema...", end=' ')
    d = datetime.datetime.now()
    PARTS_DIR = config.base["parts_dir"]

    infile = open( os.path.normpath( PARTS_DIR +  "schema.py"), "r")
    outdir = "migrations/schemas/"
    outname = modelname + "_schema.py"
    ofile = open( os.path.normpath( outdir + outname ), "w")
    ostr = infile.read()
    ostr = ostr.replace("#MODELNAME", modelname )
    ostr = ostr.replace("#DATE", d.strftime("%Y/%m/%d %H:%M:%S") )
    ofile.write(ostr)
    infile.close()
    ofile.close()
    print(" %s...(created)" % ( outdir + outname))
    
    return


if __name__ == '__main__':
    main()