
#attribut or properties
class Actuator:
 serial_number='123456'
 validity='24/12/2024'
 manufacturer='Siemens'
 inspected = ['24/10/2024','24/11/2024','24/12/2024']
 specification = {'voltage' : 220,'current' : 4,'sensitivity' : 1,'max_temp' :200,'min_temp' :0}


 def __init__(self, percentage, status):
    self.percentage = percentage
    self.status = status

 
 
 def getPercentage(self):
        return self.percentage

 def sendStatus(self):
        return self.status

 def setPercentage(self ,percentage):
       # assume that field sensor sent 20 as value for temparture
       self.percentage=percentage
 def setStatus(stat):
        status=stat
          
    
