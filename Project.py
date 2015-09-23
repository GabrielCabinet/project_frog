__author__ = 'GABI'

from core import *

class Project():
    def __init__(self,name):
        self.name = name
        print 'fdir'+ dir
        self.project_database_dictionary = read_dictionary_from_file(os.path.join(dir, 'data/project_database'))#Open project database
        print self.project_database_dictionary
        self.project_dictionary =self.project_database_dictionary.get(name,'unknown')    # Get project dictionary
        print self.project_dictionary
        print type(self.project_dictionary)
        self.root = self.project_dictionary.get('root','unknown')                            # Get root project
        self.package_list = os.listdir(self.root)                                            # List directories in root folder


project = Project('Vivarium')

print project.root
print project