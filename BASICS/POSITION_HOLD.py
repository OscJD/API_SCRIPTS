#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import api
import time
drone = api.navigation()
# wait for interface to initialize
time.sleep(3.0)

# hold position
drone.position_hold()

drone.disconnect()




"""

Class: flyt_python.API.navigation

Function: position_hold():


"""
