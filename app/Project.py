__author__ = 'GABI'

from core import *

class Project():
    def __init__(self,name):
        self.name = name
        project_database_file_path = os.path.join(script_root_dir,'data\project_database')
        print project_database_file_path
        self.project_database_dictionary = read_dictionary_from_file(project_database_file_path)#Open project database
        print self.project_database_dictionary
        self.project_dictionary =self.project_database_dictionary.get(name,'unknown')    # Get project dictionary
        print self.project_dictionary
        print type(self.project_dictionary)
        self.project_root = self.project_dictionary.get('root','unknown')                            # Get root project
        self.package_list = os.listdir(self.project_root)                                            # List directories in root folder


