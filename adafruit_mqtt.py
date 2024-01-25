import sys
from Adafruit_IO import MQTTClient

class Adafruit_MQTT:
    AIO_FEED_IDs = ["button1", 	"button2"]
    AIO_USERNAME = "NPNLab_"
    AIO_KEY = "aio_"

    def connected(self, client):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client , userdata , mid , granted_qos):
        print("Subscribeb...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit (1)

    def message(self, client , feed_id , payload):
        print("Received: " + payload)

    def __init__(self):
        client = MQTTClient(self.AIO_USERNAME , self.AIO_KEY)
        client.on_connect = self.connected
        client.on_disconnect = self.disconnected
        client.on_message = self.message
        client.on_subscribe = self.subscribe
        client.connect()
        client.loop_background()

