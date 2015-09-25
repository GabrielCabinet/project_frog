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
        self.package_name= str(package_name)
        self.root_path = project.project_root
        self.package_path = os.path.join(self.root_path,self.package_name)
        self.package_metadata_file_name = self.package_name+'_metadata.txt'
        self.package_mini_file_name = self.package_name+'_mini.jpg'
        self.package_metadata_path = os.path.join(self.package_path,self.package_metadata_file_name)

        self.package_mini_path = os.path.join(self.package_path,self.package_mini_file_name)

        if argv[0] is True:
            try:
                self.sub_folders =   ["Wip","Output","Preview"]
                self.package_kind = argv[1]
                self.package_description = argv[2]
                tasks_list_template_dic = {'Char':["Reference", "Modeling", "Shading", "Rigging", "Textures"],
                        'Prop': ["Reference", "Modeling", "Shading", "Rigging", "Textures"],
                        'Back':["Reference", "Modeling", "Shading", "Textures"],
                        'Shot': ["Animation", "Assembly", "Compositing", "FX","Layout","Layout_Anim","Lighting","Previz","Render_out"] }
                try:
                    self.tasks_list_template = tasks_list_template_dic.get(self.package_kind,'unknown')
                except:
                    msg  = self.package_name+ ': Cant get tasks list template from tasks list template dic'+str(str)
                    print msg, sys.exc_info()[0]

                self.write_package_to_disk()

            except:
                msg =  "Can't intialise paramater of the package:" + self.package_name
                print msg, sys.exc_info()[0]
        else:
            try:

                self.package_metadata_dic = read_dictionary_from_file(self.package_metadata_path)
                self.task_list = get_immediate_sub_directories(self.package_path)
            except:
                msg =  "Can't get paramater of the package:" + self.package_name
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
            msg =  self.package_name+": Can't build package metadata:"
            print msg, sys.exc_info()[0]
        try:
            self.create_package_directory()
        except:
            msg =  self.package_name+": Can't create package directory:"
            print msg, sys.exc_info()[0]
        try:
            print self.package_metadata_path
            print self.package_metadata_dic
            write_dic_to_file(self.package_metadata_path, self.package_metadata_dic)
        except:
                msg =  self.package_name+": Can't write metadata to disk:"
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
        for task in self.tasks_list_template:
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
        task_path = os.path.join(self.root_path, self.package_name, task_name)  # ROOT_PATH/PACKAGE_NAME/TASK_NAME
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


'''
package = Package('Char_TEST01',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST02',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST03',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST04',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST05',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST06',True ,'Char','Un chouette test de package' )
package = Package('Back_TEST01',True ,'Back','Un chouette test de package' )
package = Package('Back_TEST02',True ,'Back','Un chouette test de package' )
package = Package('Back_TEST03',True ,'Back','Un chouette test de package' )
package = Package('Shot_TEST01',True ,'Back','Un chouette test de package' )
package = Package('Shot_TEST02',True ,'Back','Un chouette test de package' )
package = Package('Shot_TEST03',True ,'Back','Un chouette test de package' )
package = Package('Shot_TEST04',True ,'Back','Un chouette test de package' )

'''
def list_package_tasks_directory(package_path):
        '''
        List package tasks
        :return:
        '''
        tasks_dirs = get_immediate_sub_directories(package_path)
        return tasks_dirs







