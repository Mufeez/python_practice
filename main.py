import sensor
import actuator

sensor1 =sensor.Sensor(30,True)

sensor2 = sensor.Sensor(40,True)

actuator1= actuator.Actuator(10,True)

actuator2= actuator.Actuator(0,True)


temprature1=sensor1.getTemprature()

temprature2=sensor2.getTemprature()

status1 =sensor1.getStatus()
status2=sensor2.getStatus()

if (temprature1 > 25 & status1==True):
    actuator1.setPercentage(50)

if (temprature2 > 25 & status2==True):
    actuator2.setPercentage(60)

percentage1=actuator1.getPercentage()  
percentage2=actuator2.getPercentage()

print(percentage1)
print(percentage2)



#print(temprature1,temprature2)

#print("Status of Sensor 1 " ,status1)



