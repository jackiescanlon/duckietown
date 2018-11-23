#!/usr/bin/env python
# Simple ros Aruco example. Subscribes to the camera and does stuff
import rospy
import sys
import time
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo("Received camera stream");
    cv_image = bridge.compressed_imgmsg_to_cv2(data, desired_encoding="passthrough")    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('data', gray)

def listener():

    rospy.init_node('aruco_listener')
    #rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('/howard17/camera_node/image/compressed', CompressedImage, callback)
    rospy.spin()
     

if __name__ == '__main__':
    listener()
    
    # launch the camera: roslaunch pi_camera camera_node.launch veh:=howard17
    # rosrun aruco_tags aruco_ros_python.py
    
