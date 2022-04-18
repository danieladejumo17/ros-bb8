#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

# Service callback
def callback(request):
    print("My service has been called")
    return EmptyResponse()

# Init node
rospy.init_node("service_server")

# Create service server
my_service = rospy.Service("my_service", Empty, callback)

# spin
rospy.spin()
