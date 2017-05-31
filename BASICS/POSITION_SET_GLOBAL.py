#!/usr/bin/env python
# create flyt_python navigation class instance
from flyt_python import api
import time
drone = api.navigation()
# wait for interface to initialize
time.sleep(3.0)

# send vehicle to GPS coordinate with height 10 meters above current height.
drone.position_set_global(18.7342124, 73.4323233, 10)

drone.disconnect()



"""

# Python API described below can be used in onboard scripts only. For remote scripts you can use http client libraries to call FlytOS REST endpoints from Python.

Class: flyt_python.API.navigation

Function: position_set_global(self, lat, lon, rel_ht, yaw=0.0, tolerance=0.0, async=False, yaw_valid=False):



"""
