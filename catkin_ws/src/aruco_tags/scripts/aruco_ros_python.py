#!/usr/bin/env python
# Simple ros Aruco example. Subscribes to the camera and does stuff
import rospy
import sys
import time
import cv2
import numpy as np
from std_msgs.msg import String
#from sensor_msgs.msg import CompressedImage
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    #rospy.init_node('test_listener', anonymous=True)
    # change this to subscripe to camera whatever
    #rospy.Subscriber("/howard17/camera_node/image/compressed", sensor_msgs/CompressedImage, callback)
    rospy.Subscriber("/howard17/camera_node/image/compressed", std_msgs/String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
    # our code here?
    
    

if __name__ == '__main__':
    listener()
    
    # launch the camera: roslaunch camera_node.launch veh:=howard17
    # rosrun rqt_graph rqt_graph --> look for what the camera publishes to maybe?
    # Put these files, idk somewhere?
    # launch the camera: roslaunch ros
    # rosrun duckietown ArucoRosPython.py ?
    
