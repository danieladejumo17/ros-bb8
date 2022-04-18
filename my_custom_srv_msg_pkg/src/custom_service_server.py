#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def callback(request):
    print("Received Request: Duration = {}s".format(request.duration))
    return MyCustomServiceMessageResponse(success=True)



rospy.init_node("custom_service_server")
service = rospy.Service("custom_service", MyCustomServiceMessage, callback)
rospy.spin()
