__author__ = 'GABI'

from core import *


class SessionConfig(object):
    '''
    Permet de recuperer les data utilisiateur
    '''
    def __init__(self,*argv):
        '''
        param write: Write or Reeal session config file
        param project_name: project name
        param user_name: User name

        Param has to be set in order write/project_name.user_name
        '''

        try:
            if argv[0] is True:
                self. session_project_name = argv[1]
                self.session_user_name = argv[2]
                self.write_session_config_to_disk( )
                # do something
        except:
            self.session_config_dic =  read_dictionary_from_file('D:/frog_manager_session_config.txt')
            self.session_user_name = self.session_config_dic.get('session_user','unknown')
            self.session_project_name = self.session_config_dic.get('project_name')


    def write_session_config_to_disk(self):

        dic_session_config = {'project_name' : self.session_project_name,'session_user':self.session_user_name}
        write_dic_to_file('D:/frog_manager_session_config.txt',dic_session_config)





session1=SessionConfig(True, 'Vivarium','Superman')
session2 =SessionConfig()
