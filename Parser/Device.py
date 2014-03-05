'''
Created on 21/02/2014

@author: Ivan
'''

class Device:

    def __init__(self):
        self.___id = ""
        self.___user_agent = ""
        self.___fallback = ""
        self.___actual_device_root=""
        self.___groups={}
        
    def get_id(self):
        return self.___id
    
    def get_user_agent(self):
        return self.___user_agent
    
    def get_fallback(self):
        return self.___fallback
    
    def get_actual_device_root(self):
        return self.___actual_device_root
    
    def get_groups(self):
        return self.___groups
    
    def set_id(self,id_name):
        self.___id=id_name
    
    def set_user_agent(self,user_agent):
        self.___user_agent=user_agent
    
    def set_fallback(self,fallback):
        self.___fallback=fallback
        
    def set_actual_device_root(self,actual_device):
        self.___actual_device_root=actual_device
        
    def set_groups(self, groups):
        self.___groups=groups
        
    def add_group(self,group):
        self.___groups[group.get_id()]=group
        
    