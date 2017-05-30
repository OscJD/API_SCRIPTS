#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import API
drone = API.navigation()
# wait for interface to initialize
time.sleep(3.0)

# Poll data
pos = drone.get_local_position()
# Print the data
print pos.x, pos.vx


"""

# Python API described below can be used in onboard scripts only. For remote scripts you can use http client libraries to call FlytOS REST endpoints from python.

Class: flyt_python.API.navigation

Function: get_local_position()

Response: local_position as described below.
    class local_position:
        '''
        Holds fields for local position
        '''
        x = 0.0
        y = 0.0
        z = 0.0
        vx = 0.0
        vy = 0.0
        vz = 0.0

This API support single poll mode only.


"""
