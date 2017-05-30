#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import api
import time
drone = api.navigation()
# wait for interface to initialize
time.sleep(3.0)

# Poll data
gpos = drone.get_global_position()
# Print the data
print gpos.lat, gpos.lon, gpos.alt


"""

Class: flyt_python.API.navigation

Function: get_global_position()

Response: glob_position as described below.
    class glob_position:
        '''
        Holds fields for global position
        '''
        lat = 0.0
        lon = 0.0
        alt = 0.0

This API supports single poll mode only.


"""
