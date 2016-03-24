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
from multiprocessing import Pool, Process, Lock

import SM1_States as states
##### main #####
#print "hello"

def launch_sm(node_name,root_name):
	rospy.init_node(node_name)
	random.seed()
	#smach state machine
	sm = smach.StateMachine(outcomes=['task_success'])

	#open container
	with sm:
		smach.StateMachine.add('S1', states.state_one(), transitions={'go':'S2'})
		smach.StateMachine.add('S2', states.state_two(), transitions={'go':'task_success'})


		
	sis = smach_ros.IntrospectionServer('server_name', sm, root_name)
   	sis.start()

	#execute outcome
	outcome=sm.execute()
	print "result: ", outcome

	#rospy.spin()
	sis.stop()
	return outcome


#	main()
if __name__=='__main__':

	nodes = ['node_one','node_two','node_3','node_4','node_5','node_6','node_7','node_8','node_9','node_10']
	roots = ['ROOT1','ROOT2','ROOT3','ROOT4','ROOT5','ROOT6','ROOT7','ROOT8','ROOT9','ROOT10']
#	delays=[5,10]
	for i in range(10):
		Process(target=launch_sm, args=(nodes[i], roots[i])).start()
	
