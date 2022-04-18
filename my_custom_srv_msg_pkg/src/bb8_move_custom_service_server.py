#! /usr/bin/env python

from genpy import Duration
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist

def callback(request):
    twist = Twist()
    twist.linear.x = 0.5
    twist.angular.z = 0.5

    duration = request.duration
    rate = rospy.Rate(1/duration)

    pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
    pub.publish(twist)

    rate.sleep()
    pub.publish(Twist())

    return MyCustomServiceMessage(success=True)

rospy.init("move_bb8_circle")
rospy.Service("move_bb8_in_circle_custom", MyCustomServiceMessage, callback)
rospy.loginfo("move_bb8_in_circle_custom Service Started")
rospy.spin()