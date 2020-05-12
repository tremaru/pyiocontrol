import pyiocontrol, time

myObj = pyiocontrol.panel("test2")

#myObj.setDeviceCountOnIP(2)
#print(myObj.myInt)
#print(myObj.myfloat)
#print(myObj.test)
#
#myObj.myInt = 43

myObj.mySensor = 3.1415
print(myObj.mySensor)
print(myObj.localUpdated)

while True:

    if myObj.localUpdated:
        print("OK")
    myObj.myLights = False
    myObj.mySensor += 0.01
    if myObj.siteUpdated:
        print("updated")
    #print(myObj.siteUpdated)
    time.sleep(.5)
