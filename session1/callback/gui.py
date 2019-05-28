#!/usr/bin/python3
# gui.py
# a program simulating a simple GUI main loop
# it allows to register a callback routine which is periodically called
# every 2 s
# U. Raich 26.5.2019
# this program is part of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# the program is released under GPL

import time
class DummyGUI:

    def __init__(self):
        self.count = 0
        self.callback = None
        
    def mainLoop(self):
        if self.callback == None:
            print("No callback registered, returning")
            return
        while True:
            self.callback("Hello, count= %d"%self.count)
            self.count += 1
            time.sleep(2) 
