from app import *

class GetFile:
    def __init__(self,path):
        self.path = path
        with open(self.path, 'r') as f:
            self.cf = json.loads(f.read())
        for key,val in self.cf.items():
            self.__dict__[key] = val

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def read(self):
        return self.cf

    def save(self):
        with open(self.path,'w') as f:
            f.write(json.dumps(self.cf))

