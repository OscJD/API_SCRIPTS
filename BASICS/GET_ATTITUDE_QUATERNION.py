#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import API
drone = API.navigation()
# wait for interface to initialize
time.sleep(3.0)

# Poll attitude euler data
att = drone.get_attitude_quaternion()
# Print the data
print att.x, att.y, att.z, att.w, att.rollspeed, att.pitchspeed, att.yawspeed



"""

# Python API described below can be used in onboard scripts only. For remote scripts you can use http client libraries to call FlytOS REST endpoints from python.

Class: flyt_python.API.navigation

Function: get_attitude_quaternion()

Response: attitude_quaternion as described below.
    class attitude_quaternion:
        '''
        Holds fields for Attitude data in Quaternion format
        '''
        x = 0.0
        y = 0.0
        z = 0.0
        w = 0.0
        rollspeed = 0.0
        pitchspeed = 0.0
        yawspeed = 0.0

This API supports single poll mode only.



"""
