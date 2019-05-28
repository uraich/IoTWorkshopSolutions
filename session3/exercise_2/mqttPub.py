# mqttPub.py
# a program publishing "Welcome to the AFNOG-2019 workshop" to topic
# "AFNOG19" on a PC running mosquitto
# The IP address of the PC must be known
# This is the solution to exercise 2 of session 3 of the
# workshop on IoT at the African Internet Summit 2019, Kampala, Uganda
# Copyright Uli Raich 28.5.2019
# The program is released under GPL

from umqtt.simple import MQTTClient
import network
import time

# Test reception e.g. with:
# mosquitto_sub -t "AFNOG19"

SSID="YOUR_WIFI_SSID   "             #insert your wifi ssid
WIFI_PASSORD="YOUR_WIFI_PASSWORD" #insert your wifi password

SERVER="IP_OF_MOSQUITTO_SERVER"
TOPIC=b"AFNOG19"
PAYLOAD=b"Welcome to the AFNOG-2019 workshop"

wlan=network.WLAN(network.STA_IF)
wlan.active(True)

wlan.disconnect()

print("Trying to connect to %s"%SSID)
wlan.connect(SSID,WIFI_PASSWORD)
        
while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
print("Successfully connected to WiFi network")
print('network config:', wlan.ifconfig())

c = MQTTClient("umqtt_client", SERVER)
c.connect()
for i in range(0,10):
    c.publish(TOPIC, PAYLOAD)
    time.sleep(1)
c.disconnect()
