#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import api
import time
drone = api.navigation()
# wait for interface to initialize
time.sleep(3.0)

# Poll attitude euler data
att = drone.get_attitude_euler()
# Print the data
print att.roll, att.pitch, att.yaw, att.rollspeed, att.pitchspeed, att.yawspeed



"""

# Python API described below can be used in onboard scripts only. For remote scripts you can use http client libraries to call FlytOS REST endpoints from python.

Class: flyt_python.API.navigation

Function: get_attitude_euler()

Response: attitude_euler_object as described below.
    class attitude_euler:
        '''
        Holds fields for Attitude data in Euler Angles
        '''
        roll = 0.0
        pitch = 0.0
        yaw = 0.0
        rollspeed = 0.0
        pitchspeed = 0.0
        yawspeed = 0.0

This API support single poll mode only.


"""
