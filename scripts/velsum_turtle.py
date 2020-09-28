#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

lin1 = 0
ang1 = 0
lin2 = 0
ang2 = 0

def read_vel1(data):
  global lin1, ang1
  lin1 = data.linear.x
  ang1 = data.angular.z

def read_vel2(data):
  global lin2, ang2
  lin2 = data.linear.x/4.0
  ang2 = data.angular.z/4.0

def velsum_turtle():

  rospy.init_node('velsum_turtle', anonymous=True)

  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

  vel_msg = Twist()

  rate = rospy.Rate(10)

  while not rospy.is_shutdown():

    rospy.Subscriber('/turtle1/vel_1', Twist, read_vel1)
    rospy.Subscriber('/turtle1/vel_2', Twist, read_vel2)
    
    vel_msg.linear.x = lin1 + lin2
    vel_msg.angular.z = ang1 + ang2

    pub.publish(vel_msg)

    rate.sleep()

if __name__ == '__main__':

  try:
    velsum_turtle()
  except rospy.ROSInterruptException:
    pass
