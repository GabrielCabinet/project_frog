__author__ = 'Valentin'

import re
import sys
import os
from session_config import *
from Project import *
from task import *
from comment import *
import traceback


session_config = SessionConfig()
project = Project(session_config.session_project_name)


class Package():

    '''
    Classe Package

    '''

    def __init__(self, package_name="",write=False,package_kind="",package_description="",package_tags=[]):

        '''
        :param package_name: Name of the package
        :param write: Write or Read package (TRUE)
        :type write: bool
        :param package_kind: Kind of the package (shot/bg/prop...)
        :type package_king: int
        :param description: Description of the package
        :param description: str
        :param asigned_to: User asigned to

        :return:
        '''
        self.package_name= str(package_name)
        self.root_path = project.project_root
        self.package_path = os.path.join(self.root_path,self.package_name)
        self.package_metadata_file_name = str(self.package_name)+'_metadata.txt'
        self.package_comment_file_name = str(self.package_name)+'_comment_metadata.txt'
        self.package_mini_file_name = str(self.package_name)+'_mini.jpg'
        self.package_metadata_path = os.path.join(self.package_path,self.package_metadata_file_name)
        self.package_comment_path  = os.path.join(self.package_path,self.package_comment_file_name)
        self.package_mini_path = os.path.join(self.package_path,self.package_mini_file_name)


        if write is True:
            try:
                # Get *args


                #Build the first comment for the package with creation data
                init_com = "Creation du package: %s"%(self.package_name)
                init_com += "\n Created by:%s"%(session_config.session_user_name)

                self.package_metadata_dic =  {'package_name':self.package_name,
                                              'package_king':package_kind,
                                              'description':package_description,
                                              'tags':package_tags
                                                }
                #Create directory and metadata
                os.makedirs(self.package_path)
                write_dic_to_file(self.package_metadata_path, self.package_metadata_dic)
                write_dic_to_file(self.package_comment_path,{})
                write_init_com = Comment(self.package_name,True,init_com)

            except:
                print "Can't create package:",self.package_name, traceback.format_exc()

            else:
                self.package_metadata_dic = read_dictionary_from_file(self.package_metadata_path)
                self.task_list = get_immediate_sub_directories(self.package_path)



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



def list_package_tasks_directory(package_path):
        '''
        List package tasks
        :return:
        '''
        tasks_dirs = get_immediate_sub_directories(package_path)
        return tasks_dirs







