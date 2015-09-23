__author__ = 'Gabi'

import json

class Requestable(object):

    def __init__(self, **kwargs):
        self.request_dict = kwargs

    def _add_to_request(self, **kwargs):
        self.request_dict.update(kwargs)
        return self

    def find(self):
        return json.dumps(self.request_dict, indent=4)


class Project(Requestable):

    def __init__(self,*args,**kwargs):
        super(Requestable,self)

    def get_user(self, **kwargs):
        return self._add_to_request(dict(field="user", value="current", filter=kwargs))


class User(Requestable):

    def get_packages(self, **kwargs):
        self._add_to_request(dict(field="user", value="current", filter=kwargs))

project = Project()

print project.get_user()