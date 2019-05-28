#
# cayennTempHum.py
# Connects to Cayenne and sends a dummy temperature and a dummy relative
# humidity measurement
# copyright U. Raich
# This is a demo program for the workshop  on IoT at the African Internet Summit 2019
# Released under GPL
#

import cayenne.client
import time
import logging
import random

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAMe"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

tempChannel = 0
humchannel  = 1

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
random.seed(5)

while True:    
    client.loop()
    temp = 28.0 + random.getrandbits(8)/50.
    print("Sending a temperature value of %f degrees C" % temp)
    hum = 30 + random.getrandbits(8)/10.
    print("Sending a relative humidty value of %f %% " % hum)
    client.celsiusWrite(tempChannel,temp)
    time.sleep(2)
    client.humidityWrite(humchannel,hum)
    time.sleep(2)

