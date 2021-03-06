# controls individual rgb leds on the ws2812b rgb LED
# U. Raich, 19.3.2019
# Switches all three leds off
# Solution to exercise 4 of session 2
# at the workshop on IoT at the AIS conference 2019, Kampala, Uganda
# The program is released under GPL

import machine, neopixel, time, sys

n=1        # number of LEDs

print("Switching the ws2812 rgb LED off")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    pin = 4   # connected to GPIO 4 on esp8266
else:
    print("Running on ESP32") 
    pin = 21   # connected to GPIO 21 on esp32
    
neoPixel = neopixel.NeoPixel(machine.Pin(pin), n)
    
neoPixel[0] = (0, 0, 0)
neoPixel.write()




