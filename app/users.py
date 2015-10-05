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
            self.all_user_dictionary = read_dictionary_from_file( os.path.join(script_root_dir,'data\project_database'))




        except:
            print "Error: Can't initialise user class :", sys.exc_info()[0]
            pass

        if name:

            self.user_dictionary = self.all_user_dictionary.get(name,{})
            self.password = self.user_dictionary.get('Password','unknown')
            print "Succefully initialise user class with the name:" + self.name

