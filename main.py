import sys
from Adafruit_IO import MQTTClient
import time
import random
from simpleAI import *
from uart import *

AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "CE_LHuy"
AIO_KEY = "aio_bwRE65WyeSA8AVQahdK75lAFkPgz"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " ,feed id:" + feed_id)
    if feed_id == "button1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "button2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
counterAI = 5
sensor_type = 0
aiResult = ""

while True:
    # counter = counter -1
    # if counter <= 0:
    #     counter = 10
    #     #TODO
    #     print("Random data is publishing...")
    #     if sensor_type == 0:
    #         temp = random.randint(10,20)
    #         print("Temperature...", temp)
    #         client.publish("sensor1", temp)
    #         sensor_type = 1
    #     elif sensor_type == 1:

    #         humi = random.randint(50,70)
    #         print("Humidity...", humi)
    #         client.publish("sensor2", humi)
    #         sensor_type = 2
    #     elif sensor_type == 2:

    #         light = random.randint(100, 500)
    #         print("Light...", light)
    #         client.publish("sensor3", light)
    #         sensor_type = 0
    
    # counterAI = counterAI - 1
    # if counterAI <= 0:
    #     counterAI = 5
    #     aiResult = img_detector()
    #     client.publish("AI", aiResult)    
    #     print("AI_Output: ", aiResult)

    readSerial(client)    

    time.sleep(1)
    # Listen to the keyboard for presses.
    #keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    #if keyboard_input == 27:
    #    break
