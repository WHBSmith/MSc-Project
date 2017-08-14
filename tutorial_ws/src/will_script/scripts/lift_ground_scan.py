#!/usr/bin/env python
# license removed for brevity
import rospy, time
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

if __name__ == '__main__':	
	# names this node created by script	
	rospy.init_node('talker', anonymous=True)       	 
	

	# MOVING THE TORSO	
	# topic I'm publising to
	pub = rospy.Publisher('/torso_controller/command', JointTrajectory, queue_size=10) 

    	torso_message = JointTrajectory()
        torso_message.joint_names = ['torso_lift_joint']
	torso_point = JointTrajectoryPoint()
	
	# raise up slightly
        torso_point.positions = [0.17] 
	torso_point.time_from_start = rospy.Duration(1)
	torso_message.points.append(torso_point)

	time.sleep(2)
	pub.publish(torso_message)

	
	# MOVING THE ARM
	# topic I'm publising to
	pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10) 

    	arm_message = JointTrajectory()
        arm_message.joint_names = ['arm_1_joint', 'arm_2_joint', 'arm_3_joint', 'arm_4_joint', 'arm_5_joint', 'arm_6_joint', 'arm_7_joint']
	arm_point = JointTrajectoryPoint()
	
	# home
	# aligning planes
	# [n, -1.55, n, n, y, n, y]
        arm_point.positions = [0.2, -1.55, -0.2, 1.68, -1.52, 1.2, 1] 
	arm_point.time_from_start = rospy.Duration(1)
	arm_message.points.append(arm_point)

	time.sleep(2)
	pub.publish(arm_message)

	# reach out
        arm_point.positions = [0.24, -1.55, -1.84, 1.50, -1.58, 0.08, 0]       

        time.sleep(2)
	pub.publish(arm_message)

	
	# OPEN AND CLOSE GRIPPERS
	# replace with ros service /gripper_controller/grasp
	# topic I'm publising to
	pub = rospy.Publisher('/gripper_controller/command', JointTrajectory, queue_size=10) 
	
	grip_message = JointTrajectory()
	grip_message.joint_names = ['gripper_left_finger_joint', 'gripper_right_finger_joint']
	grip_point = JointTrajectoryPoint()

	# open
	grip_point.positions = [0.04, 0.04] 
	grip_point.time_from_start = rospy.Duration(1)	
	grip_message.points.append(grip_point)

	time.sleep(2)
	pub.publish(grip_message)

	# grip
	grip_point.positions = [0.02, 0.02]

	time.sleep(2)
	pub.publish(grip_message)
	

