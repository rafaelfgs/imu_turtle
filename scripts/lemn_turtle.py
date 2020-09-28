#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import cos, sin
import time

xd = 0.0
yd = 0.0
th = 0.0

d = 0.5

k = 0.2
w = 0.4

def read_pose(data):
  global xd, yd, th
  xd = data.x + d * cos(data.theta)
  yd = data.y + d * sin(data.theta)
  th = data.theta

def set_ellipse(w, t):

  cx = 499.0/90.0
  cy = 499.0/90.0
  rx = 3
  ry = 1

  xf = rx * cos(w*t) + cx
  yf = ry * sin(w*t) + cy

  Vx = k * (xf-xd) - rx * w * sin(w*t)
  Vy = k * (yf-yd) + ry * w * cos(w*t)

  return Vx, Vy

def set_lemnscate(w, t):

  cx = 499.0/90.0
  cy = 499.0/90.0
  rx = 1
  ry = 3

  xf = rx * sin(2.0*w*t) + cx
  yf = ry * sin(w*t) + cy

  Vx = k * (xf-xd) + rx * 2.0 * w * cos(2.0*w*t)
  Vy = k * (yf-yd) + ry * w * cos(w*t)

  return Vx, Vy

def lemin_turtle():

  rospy.init_node('lemin_turtle', anonymous=True)
  pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
  rospy.Subscriber('/turtle1/pose', Pose, read_pose)

  rate = rospy.Rate(10)
  vel_msg = Twist()

  ti = time.time()

  while not rospy.is_shutdown():

    t = time.time() - ti

    # Vx, Vy = set_ellipse(w, t)
    Vx, Vy = set_lemnscate(w, t)

    vel_msg.linear.x = cos(th) * Vx + sin(th) * Vy
    vel_msg.angular.z = -(sin(th) * Vx) / d + (cos(th) * Vy) / d

    pub.publish(vel_msg)
    rate.sleep()

if __name__ == '__main__':
  try:
    lemin_turtle()
  except rospy.ROSInterruptException:
    pass
