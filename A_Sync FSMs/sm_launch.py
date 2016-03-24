#!/usr/bin/env python
import sys
sys.path.append('/opt/ros/indigo/lib/python2.7/dist-packages')
sys.path.append('/home/aransena/Python_Code_Snippets/A_Sync FSMs')
from multiprocessing import Pool, Process, Lock
import SM1 as sm

if __name__ == '__main__':
	nodes = ['node_one','node_two']
	roots = ['ROOT1','ROOT2']
	for num in range(2):
		Process(target=sm.launch_sm, args=(nodes[i], roots[i])).start()
	