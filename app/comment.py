__author__ = 'GABI'

from app.package import  *
from app.comment import *

import sys
import os.path, time
from core import *
from PySide import QtCore, QtGui


class Comment:

    def __init__(self,file):

        self.file = str(file)                  # Absolut path of the metadata.txt file
        self.comment_dictionary = read_dictionary_from_file(self.file)            # Return comment file as a dictionary

    def refresh_comment(self):
        self.comment_dictionary = read_dictionary_from_file(self.file)

    def add_comment(self, comment_dic):
        self.refresh_comment()
        update_dic_with_new_dic_to_disk(self.comment_dictionary, comment_dic, self.file)
        return

    def to_string(self):
        self.refresh_comment()
        self.comment_str = ""
        for key, value in self.comment_dictionary.iteritems():
            # data_txt =
            #data_labal = QtQui.QLabel()
            self.comment_str = "%s<P><b>%s</b>: %s </P>"%(self.comment_str, underscore_to_camelcase(key), value)
            return self.comment_str


###### TESTS #######
####################

comment = Comment('C:/Users/GABI/PycharmProjects/frog_manager_home/comment.txt')

for key in comment.comment_dictionary.keys():
    com_dic = comment.comment_dictionary.get(key,'{}')
    for com in com_dic.keys():
        print "%s:%s"%(com,com_dic[com])

comment.add_comment({
    '14':{
        'file':'test2.ma',
        'date':'24/09/1993',
        'comment': ["commentaire premiere ligne", "commentaire deuxiemme ligne"]
    },
    '13':{
        'file':'test8.ma',
        'date':'24/09/1993',
        'comment':["commentaire premiere ligne", "commentaire deuxiemme ligne"]
    }
})











