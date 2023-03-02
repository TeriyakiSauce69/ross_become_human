#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('simple_planner', anonymous = True)
	# add a publisher for sending joint position commands
	plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	# define a plan variable
	plan = Plan()
	plan_point1 = Twist()
	# just a quick solution to send two target points
	# define a point close to the initial position
	plan_point1.linear.x = -0.598
	plan_point1.linear.y = -0.127
	plan_point1.linear.z = 0.36
	plan_point1.angular.x = 3.09
	plan_point1.angular.y = 0.059
	plan_point1.angular.z = -1.57
	# add this point to the plan
	plan.points.append(plan_point1)
	
	plan_point2 = Twist()
	# define a point away from the initial position
	#Move it down!
	plan_point2.linear.x = -0.598
	plan_point2.linear.y = -0.127
	plan_point2.linear.z = 0.048
	plan_point2.angular.x = 3.09
	plan_point2.angular.y = 0.059
	plan_point2.angular.z = -1.57
	# add this point to the plan
	plan.points.append(plan_point2)
	

	plan_point4 = Twist()
	# define a point away from the initial position
	#Twist it horizontally on base
	plan_point4.linear.x = -0.598
	plan_point4.linear.y = 0.17
	plan_point4.linear.z = 0.358
	plan_point4.angular.x = 3.09
	plan_point4.angular.y = 0.059
	plan_point4.angular.z = -1.57
	# add this point to the plan
	plan.points.append(plan_point4)
	
	plan_point5 = Twist()
	# define a point away from the initial position
	#Bring it down
	plan_point5.linear.x = -0.598
	plan_point5.linear.y = 0.17
	plan_point5.linear.z = 0.05
	
	
	plan_point5.angular.x = 3.09
	plan_point5.angular.y = 0.059
	plan_point5.angular.z = -1.57
	# add this point to the plan
	plan.points.append(plan_point5)
	
	
	
	
	
	

	
	
	while not rospy.is_shutdown():
		# publish the plan
		plan_pub.publish(plan)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
