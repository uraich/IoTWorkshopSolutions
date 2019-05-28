from umqtt.simple import MQTTClient
import network
import time

# Test reception e.g. with:
# mosquitto_sub -t "AFNOG19"

SSID="YOUR_WIFI_SSID"                #insert your wifi ssid
WIFI_PASSWORD="YOUR_WIFI_PASSWORD"   #insert your wifi password

SERVER="IP_OF_MOSQUITTO_SERVER"
TOPIC=b"AFNOG19"
PAYLOAD=b"Welcome to the AFNOG-2019 workshop"

def cmdCallback(topic,payload):
    print(topic,payload)
    
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
