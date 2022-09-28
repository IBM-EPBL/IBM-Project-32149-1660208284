import random
while(True):
    t=random.randint(10,99)
    h=random.randint(10,99)
    if(t>30 and h<40):
    	print("High temperature\n")
        print("values of Temperature & Humidity is:",t,h,"Alarm is on\n")
    elif(t<30 and h>40):
    	print("Low temperature\n")
        print("values of Temperature & Humidity : ",t,h,"Alarm is off")
