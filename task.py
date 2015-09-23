__author__ = 'GABI'
from core import *

class Task:
    def __init__ (self, file):
        self.file = file
        self.task_dictionary = read_dictionary_from_file(self.file)
        self.schedule = self.task_dictionary.get('schedule','unknown')
        self.asigned_to = self.task_dictionary.get('assigned_to','unknown')
        self.statut = self.task_dictionary.get('statut','unknown')

    def refresh_task(self):
        self.task_dictionary = read_dictionary_from_file(self.file)

    def update_task(self, task_dic):
        self.refresh_task()
        update_dic_with_new_dic_to_disk(self.task_dictionary, comment_dic, self.file)
        return


task = Task('C:/Users/GABI/PycharmProjects/frog_manager_home/test_task')
print task.schedule
print task.asigned_to
print task.statut