__author__ = 'Valentin'

import re
import sys
import os

from session_config import *
from Project import *
#Hack for pycharm

session_config = SessionConfig()
project = Project(session_config.session_project_name)


class Package():
    '''
    Classe Package
    '''

    def __init__(self, package_name, *argv):

        '''
        :param package_name: Name of the package
        :param write: Write or Read package (TRUE)
        :type write: bool
        :param package_kind: Kind of the package (shot/bg/prop...)
        :type package_king: int
        :param description: Description of the package
        :param description: str

        :return:
        '''


        #----------------------
        # Init package attributs
        #---------------------
        self.package_name= str(package_name)                                                         #Prop_Pomme
        self.root_path = project.root                                                                #W:/Project_Vivarium
        self.package_path = os.path.join(self.root_path,self.package_name)                           #W:/Project_Vivarium/Prop_Pomme
        self.package_metadata_file_name = self.package_name+'_metadata.txt'                          # Props_Pomme_metadata.txt
        self.package_metadata_path = os.path.join(self.package_path,self.package_metadata_file_name) #W:/Project_Vivarium/Prop_Pomme/ # Props_Pomme_metadata.txt


        #--------------------
        #Package Write or Read
        #---------------------

        #If Write
        if argv[0] is True:
            # Init package needed attributs for writing
            try:
                self.sub_folders =   ["Wip","Output","Preview"]                  #Sub folders list
                self.package_kind = argv[1]                                      #Package kind: Char,Prop,...
                self.package_description = argv[2]                               #Package description
                
                self.package_kind_template_task_dic = {                                            # Package kind template dictionary
                        'Char': ["Reference", "Modeling", "Shading", "Rigging", "Textures"],
                        'Prop': ["Reference", "Modeling", "Shading", "Rigging", "Textures"],
                        'Back': ["Reference", "Modeling", "Shading", "Textures"],
                        'Shot': ["Animation", "Assembly", "Compositing", "FX","Layout","Layout_Anim","Lighting","Previz","Render_out"]
                               }

                # Get task template of this kind of asset.
                try:
                    self.kind_template_task_dic = self.package_kind_template_task_dic.get(self.package_kind,'unknown')  #["Reference", "Modeling",..]
                except:
                    msg =  "Can't get kind_template_dic of package kind:" + self.package_kind
                    print msg, sys.exc_info()[0]

                # Try to write package to disk
                try:
                    self.write_package_to_disk()
                except:
                    msg =  "Can't write package to disk:" + self.package_kind
                    print msg, sys.exc_info()[0]

            except:
                    msg =  "Can't create of the package:" + self.package_name
                    print msg, sys.exc_info()[0]

        # If Read
        else:
            try:

                self.package_metadata_dic = read_dictionary_from_file(self.package_metadata_path)
                self.task_list = get_immediate_sub_directories(self.package_path)

            except:
                msg =  self.package_name + ": Can't read metadata dic:"
                print msg, sys.exc_info()[0]

    def write_package_to_disk(self):
        try:
            self.package_metadata_dic =  {'package_name':self.package_name,
                                       'package_king':self.package_kind,
                                      'created_by':session_config.session_user_name,
                                      'user_who_work_on': [],
                                    'created_time':str(get_time_now()),
                                        'last_modified_time':str(get_time_now()),
                                        'description':self.package_description}
        except:
            msg =  self.package_name + ": Can't generate new metadata dic:"
            print msg, sys.exc_info()[0]
        try:
            self.create_package_directory()
        except:
            msg =  self.package_name + ": Can't create package directory"
            print msg, sys.exc_info()[0]
        try:
            write_dic_to_file(self.package_metadata_path, self.package_metadata_dic)
        except:
            msg =  self.package_name + ": Can't write metadata file"
            print msg, sys.exc_info()[0]


    def create_package_directory(self):
        '''
        Create a folder an sub_folders for EACH task
        |---- Modeling
        |-------------Wip
        |-------------Output
        |-------------Preview
        |---- Shading
        |--------------Wip
        |--------------Output
        |--------------Preview
        ect...
        :return:
        '''
        for task in self.kind_template_task_dic:
            self.create_task_folders(task_name=task)
        return True

    def create_task_folders(self,  task_name):
        '''
        Create folder and subfolder for ONE task
        |---- Modeling
        |-------------Wip
        |-------------Output
        |-------------Preview
        :param task_name: Modeling
        :return:
        '''
        # Create folder and sub_folders for one task

        # Get the path, check if folder already exist, then create it.
        task_path = os.path.join(self.root_path,self.package_name, task_name)  # ROOT_PATH/PACKAGE_NAME/TASK_NAME
        if not os.path.exists(task_path):
            os.makedirs(task_path)

            # Create the subfolder of the task
            for folder in self.sub_folders:
                folder_path = os.path.join(task_path,folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

            return True
        else:
            print "Folder already existe. Can't create task folder:"+ task_name

            return False


    def get_package_path(self):
        '''
        Return the path of a package
        :param package_name: Name of the package
        :return:
        '''
        package_path = os.path.join(self.root_path,self.package_name)  # ROOT/PACKAGE_NAME/TASK_NAME
        return  package_path

    def get_package_task_path(self,  task_name):
        '''
        Return the path of a package
        :param package_name: Name of the package
        :return:
        '''
        package_task_path = os.path.join(self.root,self.package_name,task_name)  # ROOT/PACKAGE_NAME/TASK_NAME
        return  package_task_path

    def list_package_tasks_directory(self):
        '''
        List package tasks
        :return:
        '''
        tasks_dirs = get_immediate_sub_directories(self.package_path)
        return tasks_dirs

    def list_sub_directories(self, task_name):
        '''
        List sub_folders of a task
        :return:
        '''
        sub_directories_path  = os.path.join(self.root_path,self.package_name,task_name)
        sub_directories = get_immediate_sub_directories(sub_directories_path)
        return sub_directories

    def list_sub_folder_files(self, task_name, sub_folder_name):
        files_path = os.path.join(self.root_path,self.package_name,task_name,sub_folder_name)

        files = os.listdir(files_path)
        return files


package_test = Package('testpackage4',True,'Char','Jolie petit package')

