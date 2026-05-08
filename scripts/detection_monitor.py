#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

def callback(msg):
    if len(msg.data) > 0:
        rospy.loginfo("=============================")
        rospy.loginfo("Object DETECTED!")
        rospy.loginfo(f"Object ID: {int(msg.data[0])}")
        rospy.loginfo(f"Position X: {msg.data[1]:.2f}")
        rospy.loginfo(f"Position Y: {msg.data[2]:.2f}")
        rospy.loginfo("=============================")
    else:
        rospy.loginfo("No objects detected")

rospy.init_node('detection_monitor')
rospy.Subscriber('/objects', Float32MultiArray, callback)
rospy.spin()
