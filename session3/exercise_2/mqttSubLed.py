# mqttSubLed.py
# subscribes to the "AFNOG19" topic waiting for a payload of either
# "LED on"
# or
# "LED off"
# If such a payload is seen the corresponding action is executed on the WeMos D1 built-in LED
# This is a solution to exercise 2 of session 3 for the workshop on IoT
# at the African Internet Summit 2019 in Kampala, Uganda
# Copyright Uli Raich, 28. May 2019
# The program is released under GPL

from umqtt.simple import MQTTClient
from machine import Pin
import network
import time11

led=Pin(2,Pin.OUT)

# Test reception e.g. with:
# mosquitto_sub -t "AFNOG19"

SSID="YOUR_WIFI_SSID"               #insert your wifi ssid
WIFI_PASSWORD="YOUR_WIFI_PASSWORD"  #insert your wifi password

SERVER="IP_OF_MOSQUITTO_SERVER "
TOPIC=b"AFNOG19"

def cmdCallback(topic,payload):
    print(topic,payload)
    if payload == b"LED on":
        led.value(0)
        print("Switch LED on")
    elif payload == b"LED off":
        led.value(1)
        print("Switch LED off");
        
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

c.set_callback(cmdCallback)
c.subscribe("AFNOG19")

while True:
    c.wait_msg()
