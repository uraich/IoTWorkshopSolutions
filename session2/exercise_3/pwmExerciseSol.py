# pwmExerciseSol.py controls the light intensity of the built-in LED using PWM
# This is the solution to exercise 3 of session 2
# It is essentially the program described in chapter 7 of the
# Micropython tutorial for the ESP8266. Both, ESP8266 and ESP32 use GPIO 2 to control the LED
# copyright: U. Raich, 12.5.2019
# This program is part of the workshop on IoT at the AIS conference 2019, Kampala, Uganda
# released under GPL

from machine import Pin,PWM
import time

# sends a cycle of light intensities on a triangular curve
        
def intensityCycle(duration,resolution):
    
    for i in range(0,resolution-1):
        brightness = 1023 - 1023/resolution*i
#        print(brightness)        
        pwmLED.duty(round(brightness))
        time.sleep_ms(duration)
        
    for i in range(0,resolution-1):
        brightness = 1023/resolution * i
#        print(brightness)
        pwmLED.duty(round(brightness))
        time.sleep_ms(duration)
          
print("Changing the light intensity on the built-in LED using PWM")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

led = Pin(2)

pwmLED = PWM(led)
pwmLED.freq(1000)      # PWM at 1 kHz

for i in range(0,10):
    intensityCycle(20,100)
# switch PWM off
pwmLED.deinit()
# switch led off 
led.value(1)