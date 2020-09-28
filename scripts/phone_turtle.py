#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist

lin = 0
ang = 0

def read_vel(data):

    global lin, ang

    front = data.linear_acceleration.z - data.linear_acceleration.y
    side = data.linear_acceleration.x

    if side > 2.0:
        ang = side/2.0 - 1.0
    else:
        if side < -2.0:
            ang = side/2.0 + 1.0
        else:
            ang = 0.0

    if front > 2.0:
        lin = front/2.0 - 1.0
    else:
        if front < -2.0:
            lin = front/2.0 + 1.0
        else:
            lin = 0.0

def phone_turtle():

    rospy.init_node('phone_turtle', anonymous=True)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    vel_msg = Twist()

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        rospy.Subscriber('/phone1/android/imu', Imu, read_vel)

        vel_msg.linear.x = lin
        vel_msg.angular.z = ang

        pub.publish(vel_msg)

        rate.sleep()

if __name__ == '__main__':

    try:
        phone_turtle()
    except rospy.ROSInterruptException:
        pass
