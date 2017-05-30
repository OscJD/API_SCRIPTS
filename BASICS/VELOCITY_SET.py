#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import api
import time
drone = api.navigation()
# wait for interface to initialize
time.sleep(3.0)

# fly towards right ( with respect to vehicle current heading) 
drone.velocity_set(0, +2, 0, body_frame=True)



"""

# Python API described below can be used in onboard scripts only. For remote scripts you can use http client libraries to call FlytOS REST endpoints from Python.

Class: flyt_python.API.navigation

Function: velocity_set(self,vx, vy, vz, yaw_rate=0.0, tolerance=0.0, relative=False, async=False, yaw_rate_valid=False, body_frame=False):



"""
