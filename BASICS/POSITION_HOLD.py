#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import API
drone = API.navigation()
# wait for interface to initialize
time.sleep(3.0)

# hold position
drone.position_hold()




"""

Class: flyt_python.API.navigation

Function: position_hold():


"""
