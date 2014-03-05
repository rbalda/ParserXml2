import Capability
import Device
import Group
from thread import get_ident

def searchDevices(line):
    return line.find('<devices>')

def searchEndDevices(line):
    return line.find('</devices>')

def searchDevice(line):
    return line.find('<device ')

def searchEndDevice(line):
    return line.find('</device>')

def searchGroup(line):
    return line.find('<group ')

def searchEndGroup(line):
    return line.find('</group>')      

def extractDeviceId(line):
    start=line.rfind('id="')+4
    end=line.rfind('" user_agent')
    return line[start:end]

def extractGroupId(line):
    start=line.rfind('id="')+4
    end=line.rfind('">')
    return line[start:end]
        

def extractDeviceUserA(line):
    start=line.rfind('user_agent="')+12
    end=line.rfind('" fall_back')
    print line[start:end]
    return line[start:end]

def extractDeviceFallB(line):
    start=line.rfind('fall_back="')+11
    
    if line.rfind('" actual')!=-1:
        end=line.rfind('" actual')
    else:
        end=line.rfind('">')
    temp = line[start:end]
    return temp

def extract_actualDevice(line):
    if line.rfind('actual_device_root')!=-1:
        start=line.rfind('actual_device_root="')+20
        end=line.rfind('">')
        return line[start:end]
    else:
        return ''
        

def extractDeviceAtt(line,device):
    device.set_id(extractDeviceId(line))
    device.set_user_agent(extractDeviceUserA(line))
    device.set_fallback(extractDeviceFallB(line))
    device.set_actual_device_root(extract_actualDevice(line))
    
def extractGroupAtt(line,device):
    group=Group.Group()
    start=line.rfind('id="')+4
    end=line.rfind('">')
    group.set_id(line[start:end])
    device.add_group(group)
    
#Obtiene el capability de cada tag <capability=#
def searchCapability(line):
    return line.find("<capability ")

    
def extractNameCapability(line,capability):
    start=line.rfind('name="')+6
    end=line.rfind('" value="')
    capability.set_name(line[start:end])
    
def extractValueCapability(line,capability):
    start=line.rfind('value="')+7
    end=line.rfind('"/')
    capability.set_value(line[start:end])
    
def addCapabilities(group,capability):
    group.add_capabilities(capability)
    
def addHeriarchy(devices):
    for key in devices.keys():
        temp = devices.get(key).get_fallback()
        if devices.has_key(temp):
            x=devices.get(key).get_groups()
            y=devices.get(temp).get_groups()
            z=dict(y.items()+x.items())
            devices.get(key).get_groups().update(z)
            
def searchHeriarchy(key):
    print devices.get(key).get_id()     
    temp = devices.get(key).get_fallback()
    
    while devices.has_key(temp):
        print devices.get(temp).get_id()
        temp = devices.get(temp).get_fallback()
        
def ingrese():
    key= raw_input("Ingrese id: ")
    #str(key)
    #searchHeriarchy(key)
    while key!='':
        key=raw_input("Ingrese id: ")
        searchHeriarchy(key)
               
        
        

    
        
        
def read_Xml(devices):
    inTagGroup=False
    inDevicesContent=False
    inTagDevice=False
    #xmlFile=open('prueba.xml','r')
    xmlFile=open('wurfl-2.3.xml','r')
    line = xmlFile.readline()
    while line!='':
        line=xmlFile.readline()
        if not(inDevicesContent):
            if searchDevices(line)!=-1:
                inDevicesContent=True
        else:
            if not(inTagDevice):
                if searchDevice(line)!=-1:
                    #Instancia de dispositivo provisional hasta que se finalic el tag
                    device=Device.Device()
                    inTagDevice=True                    
                    extractDeviceAtt(line,device)
            else:
                if not(inTagGroup):
                    if searchGroup(line)!=-1:
                        inTagGroup=True
                        temp=extractGroupId(line)
                        extractGroupAtt(line,device)                                              
                else:
                    if searchCapability(line)!=-1:
                                capability=Capability.Capability();
                                extractNameCapability(line, capability)
                                extractValueCapability(line, capability)
                                addCapabilities(device.get_groups().get(temp),capability)                   
                    if searchEndGroup(line)!=-1:
                        inTagGroup=False
                if searchEndDevice(line)!=-1:                    
                    devices[device.get_id()]=device
                    inTagDevice=False
            if searchEndDevices(line)!=-1:
                inDevicesContent=False
                
                
if __name__ == "__main__":
    devices={}
    read_Xml(devices)
    addHeriarchy(devices)
    ingrese()

    