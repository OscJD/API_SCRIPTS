#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import API
drone = API.navigation()
# wait for interface to initialize
time.sleep(3.0)

# takeoff over current location 
drone.take_off(6.0)


"""

Class: flyt_python.API.navigation

Function: take_off(self, takeoff_alt=5.0):


"""
