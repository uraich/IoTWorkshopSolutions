#
# cayenneConnect.py
# Connects to Cayenne
# copyright U. Raich
# This is a demo program for the workshop  on IoT at the African Internet Summit 2019
# Released under GPL
#

import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)

while True:
    client.loop()
    time.sleep(1)

