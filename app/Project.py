__author__ = 'GABI'

from core import *
import os
class Project():
    def __init__(self,name):
        script_root_dir = os.path.abspath(__file__ + "/../../")

        project_database_file_path = os.path.join(script_root_dir,'data\project_database')

        self.project_database_dictionary = read_dictionary_from_file(project_database_file_path)#Open project database

        self.project_dictionary =self.project_database_dictionary.get(name,{})    # Get project dictionary

        self.project_root = self.project_dictionary.get('root','unknown')                            # Get root project


        if self.project_root == "unknown":
            return
        else:

            self.package_list = os.listdir(self.project_root)                                            # List directories in root folder


