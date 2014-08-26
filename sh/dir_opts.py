
import os

from os.path import (
    join as py_join,
    isdir as py_isdir,
    exists as py_exists
)

from SHException import SHException
from join_listlike import join_listlike

def change_dir(options, arguments):    
    
    path = join_listlike({}, arguments)
    os.chdir(path)
    
def file_exists(options, arguments):
    
    path = join_listlike({}, arguments)
    return py_exists(path)

def make_dir_p(options, arguments):
    #print "arguments: ", arguments
    if 'parents' in options and options['parents']:
        
        whole = ""

        for part in join_listlike({"as_list": True}, arguments):
            #print "part, ", part, ", whole, ", whole
            if whole == "" and part[1] == ':':
                whole = part
            else:
                whole += "/%s" % part
            
            if not py_exists(whole):
                os.mkdir(whole)
            if not py_isdir(whole):
                raise SHException("File exists at %s" % whole)
    else:
        
        path = join_listlike({},arguments)
        try:
            os.mkdir(path)
        except Exception, e:
            raise SHException(e.message)
        
def remove_rf(options, arguments):
    
    path = join_listlike({}, arguments)
    os.remove(path)
