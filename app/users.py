from core import *
import sys

class User:

    def __init__(self, name):
        """
        Initialise class attribut
        :param sself:
        :param name: User name
        :return:
        """

        try:

            self.name = name
            self.all_user_dictionary = read_dictionary_from_file('C:/Users/GABI/PycharmProjects/frog_manager_home/user_database.txt')


            self.user_dictionary = self.all_user_dictionary.get(name,'unknown')
            self.password = self.user_dictionary.get('Password','unknown')
            print "Succefully initialise user class"
        except:
            print "Error: Can't initialise user class :", sys.exc_info()[0]
            pass


# TEST
current_user = User('Victor')
print "USERS TEST "
print "****************************"
print "All user dic \n"+ str(current_user.all_user_dictionary)
print current_user.password
print "****************************"


