from core import *
import sys

class User:

    def __init__(self, name=""):
        """
        Initialise class attribut
        :param sself:
        :param name: User name
        :return:
        """

        try:

            self.name = name
            self.all_user_dictionary = read_dictionary_from_file(r'C:\Users\GABI\PycharmProjects\project_frog\data\project_database')

            self.user_dictionary = self.all_user_dictionary.get(name,{})

            self.password = self.user_dictionary.get('Password','unknown')

            print "Succefully initialise user class with the name:" + self.name
        except:
            print "Error: Can't initialise user class :", sys.exc_info()[0]
            pass

