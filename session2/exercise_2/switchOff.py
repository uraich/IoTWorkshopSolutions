#
# solution to exercise 2 session 2-b
# switching the built-in led off
# Copyright Uli Raich
# This program is part of a workshop on IoT
# at the African Internet Summit 2019, Kampala, Uganda
# The program is released under GPL

from machine import Pin
import time

led = Pin(2,Pin.OUT)
print("Switching led off!")
led.value(1)

while True:
    time.sleep(10)   # sleep forever

