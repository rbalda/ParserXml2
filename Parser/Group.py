'''
Created on 21/02/2014

@author: Ivan
'''

class Group:  


    def __init__(self):
        self.___id=""
        self.___capabilities={}
        
    def get_id(self):
        return self.___id
    
    def get_capabilities(self):
        return self.___capabilities
        
    def set_id(self,id_name):
        self.___id=id_name
    
    def set_capabilities(self,capabilities):
        self.___capabilities=capabilities
        
    def add_capabilities(self,capability):
        self.___capabilities[capability.get_name()]=capability