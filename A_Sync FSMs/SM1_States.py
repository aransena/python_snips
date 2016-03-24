#!/usr/bin/env python
import time
import random 
import sys
sys.path.append('/opt/ros/indigo/lib/python2.7/dist-packages')
sys.path.append('/home/aransena/Python_Code_Snippets/A_Sync FSMs')
#import roslib; roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
import threading


class state_one(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['go'])

	def execute(self, userdata):
		rospy.loginfo('Executing state S1')
		time.sleep(10)
		return 'go'

class state_two(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['go'])

	def execute(self, userdata):
		rospy.loginfo('Executing state S2')
		time.sleep(10)
		return 'go'

