#!/usr/bin/env python
import time
import random 

import roslib; roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
import threading


class state_one(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['exit'])

	def execute(self, userdata):
		rospy.loginfo('Executing state ERR')
		time.sleep(1)
		return 'exit'

