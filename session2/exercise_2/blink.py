#
# solution to exercise 2 session 2
# blinking the built-in led
# Copyright Uli Raich
# This program is part of a workshop on IoT
# at the African Internet Summit 2019, Kampala, Uganda
# The program is released under GPL

from machine import Pin
import time

led = Pin(2,Pin.OUT)
state = True

while True:
    # led is active low
    if (state):
        print("led is off")
    else:
        print("led is on")
    led.value(state)
    time.sleep(0.5)    # sleep for 500 ms
    state =  not state
