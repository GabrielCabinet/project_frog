__author__ = 'GABI'

from app.package import  *

import uuid
import sys
import os.path, time
from core import *
from PySide import QtCore, QtGui

session_config = SessionConfig()
project = Project(session_config.session_project_name)
class Comment:

    def __init__(self,package_name,write=False,comment_txt=""):

        self.comment_file_name = "%s_comment.txt"%(package_name)
        self.comment_file_path = os.path.join(project.project_root,package_name,self.comment_file_name)
        if write is True:
            self.new_comment_dic = {str(uuid.uuid4()):
                {
                    "user":session_config.session_user_name,
                    "comment": comment_txt,
                    "date": str(get_time_now()),
                    "file": "unknown"}
                }

            try:
                comment_dic = read_dictionary_from_file(self.comment_file_path)
                update_dic_with_new_dic_to_disk(comment_dic, self.new_comment_dic, self.comment_file_path )
            except:
                msg =  "Can't write comment dic of the package to file:" + str(self.comment_dictionary)
                print msg, sys.exc_info()[0]
        else:
            self.comment_dictionary = read_dictionary_from_file( self.comment_file_path)            # Return comment file as a dictionary

    def refresh_comment(self):
        self.comment_dictionary = read_dictionary_from_file( self.comment_file_path)

    def add_comment(self, comment_dic):
        self.refresh_comment()
        update_dic_with_new_dic_to_disk(self.comment_dictionary, comment_dic,self.comment_file_path)
        return

    def to_string(self):
        self.refresh_comment()
        self.comment_str = ""
        for key, value in self.comment_dictionary.iteritems():
            # data_txt =
            #data_labal = QtQui.QLabel()
            self.comment_str = "%s<P><b>%s</b>: %s </P>"%(self.comment_str, underscore_to_camelcase(key), value)
            return self.comment_str









