#!/usr/bin/python3
# callbackDemo.py
# registers a callback and then calls dummy a GUI main loop
# every 2 s
# U. Raich 26.5.2019
# this program is part of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# the program is released under GPL

from gui import DummyGUI

def helloCallback(msg):
    print(msg)

myGUI = DummyGUI()
myGUI.callback = helloCallback
myGUI.mainLoop()
