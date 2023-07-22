
#attribut or properties
class Sensor:
 serial_number='123456'
 validity='24/12/2024'
 manufacturer='Siemens'
 inspected = ['24/10/2024','24/11/2024','24/12/2024']
 specification = {'voltage' : 220,'current' : 4,'sensitivity' : 1,'max_temp' :200,'min_temp' :0}


 def __init__(self, temprature, status):
    self.temprature = temprature
    self.status = status

 
 
 def getTemprature(self):
        return self.temprature

 def getStatus(self):
        return self.status

 def setTemprature():
       # assume that field sensor sent 20 as value for temparture
       temprature = 20
 def setStatus(stat):
        status=stat
          
    
