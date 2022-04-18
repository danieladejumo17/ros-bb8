#! /usr/bin/env python

from numpy import rate
import rospy
from geometry_msgs.msg import Twist

class MoveBB8:
    def __init__(self):
        self.bb8_vel_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        while not self.ctrl_c:
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                rate.sleep()

    def shutdownhook(self):
        self.ctrl_c = True

    def move_bb8(self, linear_speed=0.2, angular_speed=0.2):
        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed

        self.loginfo("Moving BB8!")
        self.publish_once_in_cmd_vel()


if __name__ == "__main__":
    rospy.init_node("move_bb8_test", anonymous=True)
    movebb8_object = MoveBB8()
    try:
        movebb8_object.move_bb8()
    except rospy.ROSInterruptException:
        pass