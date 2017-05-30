#!/usr/bin/env python

# create flyt_python navigation class instance
from flyt_python import API
drone = API.navigation()
# wait for interface to initialize
time.sleep(3.0)

# land at current location. Return after landed
drone.land(async=False)

# land at current location. Function returns immediately and land action finishes asynchronously.  
drone.land(async=True)

"""

# Python API described below can be used in onboard scripts only. For remote scripts you can use http client libraries to call FlytOS REST endpoints from python.

Class: flyt_python.API.navigation

Function: land(async=False):



"""
