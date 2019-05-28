#
# cayenneDummyMeas.py
# Connects to Cayenne and sends a dummy temperature measurement
# The temperature is 28 °C + a random number 0 .. 2.55 °C
# copyright U. Raich
# This is a demo program for the workshop  on IoT at the African Internet Summit 2019
# Released under GPL
#

import cayenne.client
import time
import logging
import random

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USER_NAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

tempChannel=0

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
random.seed(5)

while True:    
    client.loop()
    temp = 28.0 + random.getrandbits(8)/50.
    print("Sending a temperature value of %f degrees C" % temp)
    client.celsiusWrite(tempChannel,temp)
    time.sleep(5)

