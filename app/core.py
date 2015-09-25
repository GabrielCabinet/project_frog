__author__ = 'GABI'

import os
import ast
import sys
import json
import pprint
from datetime import datetime
script_root_dir = os.path.abspath(__file__ + "/../../")


"""
PROCESS DICTIONARY
"""
'''
    def list_packages(self, name_filter="", task_filter=""):
    '''
'''
    List package using optional filter
    :param name_filter: use '*' as a wild card before or after the name
    :type name_filter: str
    :param task_filter: Array of task package MUST have.
    :type task_filter: list
    '''
'''
    self.session_config = SessionConfig()
    self.project = Project(session_config.session_project_name)
    self.project_root = self.project.project_root                 #W:/Vivarium
    self.list_package = os.listdir(self.project_root)             # List all package in root directory

    #Filter by name
    if name_filter:
    # Filter list of packages
        self.list_package = [package for package in list_package if
        re.findall("^%s$" % name_filter.lower().replace("*", ".+"), package.lower())]
        # Return List of Package matching Name Filter

        #Filter by task_filter
        if task_filter:
            remove_list = []
            for package in self.list_package:
                list_package_task = list_package_tasks_directory(os.path.join(project_root,package))
                print "%s,%s"%(package , list_package_task)
                for task in task_filter:
                    if task not in list_package_task:
                            remove_list.append(package)
                self.list_package = [package for package in self.list_package if package not in remove_list ]





            return self.list_package

'''

def clearLayout(layout):
    #http://josbalcaen.com/maya-python-pyqt-delete-all-widgets-in-a-layout/
    '''
    Clean pyside layout
    :param layout:
    :return:
    '''
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())

def underscore_to_camelcase(text):
    """
    Converts underscore_delimited_text to camelCase.
    Useful for JSON output
    """
    return ''.join(word.title()  for i, word in enumerate(text.split('_')))

def get_time_now():
    now = datetime.now().time()

    return now

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def list_packages(self, name_filter="", task_filter=""):
    '''
    List package using optional filter
    :param name_filter: use '*' as a wild card before or after the name
    :type name_filter: str
    :param task_filter: Array of task package MUST have.
    :type task_filter: list
    '''
    self.session_config = SessionConfig()
    self.project = Project(session_config.session_project_name)
    self.project_root = self.project.project_root                 #W:/Vivarium
    self.list_package = os.listdir(self.project_root)             # List all package in root directory

    #Filter by name
    if name_filter:
    # Filter list of packages
        self.list_package = [package for package in list_package if
        re.findall("^%s$" % name_filter.lower().replace("*", ".+"), package.lower())]
        # Return List of Package matching Name Filter

        #Filter by task_filter
        if task_filter:
            remove_list = []
            for package in self.list_package:
                list_package_task = list_package_tasks_directory(os.path.join(project_root,package))
                print "%s,%s"%(package , list_package_task)
                for task in task_filter:
                    if task not in list_package_task:
                            remove_list.append(package)
                self.list_package = [package for package in self.list_package if package not in remove_list ]





            return self.list_package
def convert_str_to_dic(str):
    """
    COnvert string to dictionary
    :param str: string
    :return:
    """
    """
    :param str:
    :return:
    """
    try:
        dic = ast.literal_eval(str)
    except:
        msg  = 'Cant convert str to dic'+str(str)
        print msg, sys.exc_info()[0]
    return dic

"""
INPUT/OUTPUT
"""



def read_text_file(file):
    """
    Read and return a string from a text file.
    :param file:
    :return:
    """
    try:
        file_open = open(file,'r')
        file_text = str(file_open.read())
        return file_text
    except IOError as e:
        print "{0}".format(e)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

def create_text_file(file, file_text):
    '''
    Write a text file to disk
    :param file: absolute path of the file
    :param file_text: String to write
    :return:
    '''
    try:
        with open(file, 'w') as proc_seqf:
            proc_seqf.write(file_text)
    except IOError as e:
        print "{0}".format(e)
    except:
        print "Unexpected error while writing file_text to disk:", sys.exc_info()[0]
        raise

def read_dictionary_from_file(file):
    try:
        file_string = read_text_file(file)                             # Read D:/metadata.txt
        dictionary = convert_str_to_dic(file_string)
        return dictionary

    except:
        print "Can't read dictionary from fitle:", sys.exc_info()[0]

        return {}

def write_dic_to_file(file, dic):
    '''
    Write a text file to disk
    :param file: absolute path of the file
    :param dic: dic to write
    :return:
    '''
    try:
        with open(file, 'w') as f:
            dic_format_json = json.dumps(dic,sort_keys=True,indent=4)
            f.write(dic_format_json)
    except IOError as e:
        print "{0}".format(e)
    except:
        print "Unexpected error while writing file_text to disk:", sys.exc_info()[0]
        raise

def update_dic_with_new_dic_to_disk(dic, new_dic, file ):
    '''
    Update dictionary by writing or overwriting a metadata into the metadata dictionary
    :param dic: A dictionary{key,value} to be updated    #{'last_modified':'20/09/1993'}
    :type dic: dict
    :param new_dic: A dictionary (key,value) of the update to perform
    :type new_dic: dict
    :param file: Path of file Input/Output
    :type file: str
    :return

    '''
    try:
        updated_dictionary = merge_two_dicts(dic, new_dic)        # Merge dictionary
        if isinstance( updated_dictionary, dict):
            write_dic_to_file(file,  updated_dictionary)                                     # I/O Output
        else:
            raise TypeError("'new_dic' can only be a dict \t Actual Type:"+type(new_dic) )
    except:
        print "Can't update dictionary:", sys.exc_info()[0], 'dic', str(dic), 'new_dic', str(new_dic), 'file',str(file)


"""
QUERY OS
"""

def get_immediate_sub_directories(path):
    return [dir_name for dir_name in os.listdir(path)
            if os.path.isdir(os.path.join(path, dir_name))]

def list_directory(d):
    return  os.listdir(d)

def get_last_modified_time(file):
    '''
    Return the last date modification
    :param file: absolute path           # D:/file
    :return:
    '''
    return time.ctime(os.path.getmtime(file))

def get_created_time(file):
    '''
    Return the last date modification
    :param file: absolute path           # D:/file
    :return:
    '''
    return time.ctime(os.path.getctime(file))


"""
QUERY MANAGER
"""

def get_current_user_name():
    '''
    Try to get current user_name
    :return:
    '''
    try:
        current_user_name = current_user.name
        return current_user_name
    except:
        print "Can't get current user:", sys.exc_info()[0]
        return 'unknown'





