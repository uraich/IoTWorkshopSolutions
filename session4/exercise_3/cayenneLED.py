#
# cayenneLED.py
# gets command information from a Cayenne button and switches on/off the
# built-in LED on the WeMos D1 CPU card
# copyright U. Raich
# This is a demo program for the workshop  on IoT at the African Internet Summit 2019
# Released under GPL
#
from machine import Pin
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

global ledChannel
global builtinLed
ledChannel = 9
builtinLed = Pin(2,Pin.OUT)

# callback routine to treat command messages from Cayenne
def on_message(message):
    global ledChannel
    msg = cayenne.client.CayenneMessage(message[0],message[1])
    if msg.channel == ledChannel:
        if int(msg.value) == 1:         # the builtin LED is actice low
            builtinLed.value(0)
        else:
            builtinLed.value(1)
        if int(msg.value) == 1:
            print("Switching built-in led on");
        else:
            print("Switching built-in led off");
    return

# switch LED off
builtinLed.value(1)                # active low

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# register callback
client.on_message=on_message

while True:
    client.loop()
    time.sleep(1)

