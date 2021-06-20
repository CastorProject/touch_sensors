#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import Int32MultiArray

class touchSensorNode(object):
	def __init__(self, name):
		self.name = name
		rospy.init_node(self.name)
		self.rate = rospy.Rate(50)
		self.initSubscribers()
		self.initPublishers()
		self.initVariables()
		return

	def initSubscribers(self):
		self.touchSensorsSub = rospy.Subscriber("/touchSensors", Int32MultiArray, self.callbackTouchSensors)
		return

	def initPublishers(self):
		return

	def initVariables(self):
		self.touchSensors = [0,0,0,0,0,0,0,0,0,0,0,0]
		return

	#Callbacks
	def callbackTouchSensors(self, msg):
		self.touchSensors = msg.data
		return

	#Main
	def main(self):
		rospy.loginfo("[%s] touchSensor node started ok", self.name)
		self.rate.sleep()
		while not (rospy.is_shutdown()):
			print(self.touchSensors)
		return

if __name__=='__main__':
	ts = touchSensorNode("sensorsNode")
	ts.main()
