__author__ = 'GABI'
from core import *
from session_config import *
from Project import  *
from users import *
session_config = SessionConfig()
project = Project(session_config.session_project_name)


class Task:
    def __init__ (self,package_name,task_name, write=False,statut='wip',schedule="",asigned_to=""):

        self.task_path = os.path.join(project.project_root,package_name,task_name)
        self.task_path_metadata_filename = "%s_%s_metadata.txt"%(package_name,task_name)
        self.task_path_metadata_filepath = os.path.join(self.task_path, self.task_path_metadata_filename)

        if write is True:
            self.created_by = session_config.session_user_name
            self.created_time = get_time_now()
            self.statut = statut
            self.task_name = task_name

            #Build task dictionary

            self.schedule = schedule
            self.last_user = session_config.session_user_name
            self.last_edited_time= get_time_now()
            self.asigned_to = asigned_to
            self.task_dictionary = {
                                    'task_name':self.task_name,
                                    'statut':self.statut,
                                    'schedule':self.schedule,
                                    'asigned_to':self.asigned_to,
                                    'last_user':self.last_user,
                                    'last_edited_time':str(self.last_edited_time),  #CAREFUL ! datetime.time() is not JSON serializable
                                    'created_by':str(self.created_time)
                                    }
            write_dic_to_file(self.task_path_metadata_filepath,self.task_dictionary)

        else:
            self.task_dictionary = read_dictionary_from_file(self.task_path_metadata_filepath)
            self.schedule = self.task_dictionary.get('schedule','unknown')
            self.asigned_to = self.task_dictionary.get('assigned_to','unknown')
            self.statut = self.task_dictionary.get('statut','unknown')
            self.last_user = self.task_dictionary.get('last_user','unknown')
            self.last_edited_time = self.task_dictionary.get('last_edited_time','unknown')
            self.created_by = self.task_dictionary.get('created_by','unknown')
    def refresh_task(self):
        self.task_dictionary = read_dictionary_from_file(self.file)

    def update_task(self, task_dic):
        self.refresh_task()
        update_dic_with_new_dic_to_disk(self.task_dictionary, comment_dic, self.file)
        return

