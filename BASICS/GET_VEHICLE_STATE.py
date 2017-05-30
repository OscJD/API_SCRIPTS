#!/usr/bin/env python

# create flyt_python navigation class instance

from flyt_python import api
import time
drone = api.navigation()
time.sleep(3.0)

# get arm status
print drone.is_armed()
print drone.get_vehicle_mode()



"""

# Python API for vehicle state is split into two APIs

# Check arm status
Class: flyt_python.API.navigation
Function Definition: is_armed()
Arguments: None
return: Boolean

# Check vehicle mode
Class: flyt_python.API.navigation
Function Definition: get_vehicle_mode()
Arguments: None
return: string


"""
