
import serial.tools.list_ports
import sys
import time

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        # print(port, "\n")
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    print (commPort)
    # return commPort
    # return "COM3"
    return "/dev/pts/5"
    # pass
    

# if getPort() != "None" :
ser = serial.Serial( port = getPort(), baudrate=115200)   
#ser = serial.Serial( port = "/dev/pts/3", baudrate=9600)   
print(ser)

def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("sensor1", splitData[2])
    elif splitData[1] == "H":
        client.publish("sensor2", splitData[2])
    elif splitData[1] == "L":
        client.publish("sensor3", splitData[2])
        
mess = ""
def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        #print(mess)
        while ("#" in mess) and ("!" in mess):
            start = mess.find("#")
            end = mess.find("!")
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def writeData(data):
    ser.write(str(data).encode())
    print (data)
