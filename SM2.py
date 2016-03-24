#!/usr/bin/env python
import time
import random 

import roslib; roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
import threading


##### main #####

def main():
	rospy.init_node('FB1_state_machine')
	random.seed()
	#smach state machine
	sm = smach.StateMachine(outcomes=['task_success','task_fail', 'task_error'])

	#open container
	with sm:
		smach.StateMachine.add('S0_READ', states.read_rsbb(), transitions={'proceed':'S1_CALIBRATE',
																	'error':'ERR'})


		
	sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
   	sis.start()

	#execute SM
	outcome=sm.execute()
	print "result: ", outcome
	rospy.spin()
	sis.stop()

if __name__=='__main__':
	main()
