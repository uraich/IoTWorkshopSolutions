# ws2812ColorCycle.py: cycles the colors on a ws2812b rgb led
# U. Raich, 19.3.2019
# This program is the solution to exercise 5 of session of the
# workshop on IoT at the AIS conference 2019, Kampala, Uganda
# The program is released under GPL

import machine, neopixel, time, sys

n=1        # number of LEDs

print("Color cycling the ws2812 rgb LED")
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
for i in range (0,250,5):
    for j in range(0,250,5):
        for k in range(0,250,5):
            neoPixel[0] = (j, i, k)
            neoPixel.write()
#            time.sleep_ms(10)
#            print("r,g,b: %d %d %d"%(j,i,k))

neoPixel[0] = (0, 0, 0)
neoPixel.write()




