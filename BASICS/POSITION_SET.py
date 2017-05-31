#!/usr/bin/env python
# create flyt_python navigation class instance
from flyt_python import api
import time
drone = api.navigation()
# wait for interface to initialize
time.sleep(3.0)

# command vehicle towards 5 meteres SOUTH from current location regardless of heading
drone.position_set(-5, 0, 0, relative=True)

drone.disconnect()

""""

# Python API described below can be used in onboard scripts only. For remote scripts you can use http client libraries to call FlytOS REST endpoints from python.

Class: flyt_python.API.navigation

Function: position_set(self, x, y, z, yaw=0.0, tolerance=0.0, relative=False, async=False, yaw_valid=False,
                     body_frame=False):


"""
