#!/usr/bin/env python
# Simple ros Aruco example. Subscribes to the camera and does stuff
import rospy
import sys
import time
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
def callback(data):
    br = CvBridge()
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #rospy.loginfo("Received camera stream");
    frame = br.compressed_imgmsg_to_cv2(data)    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cvshutdown()

    
def listener():
    br = CvBridge()
    print('Running listener')
    rospy.init_node('aruco_listener')
    #rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('/howard17/camera_node/image/compressed', CompressedImage, callback)
    rospy.spin()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cvshutdown()
    
 

def cvshutdown():
    cv2.destroyAllWindows()

if __name__ == '__main__':
    listener()
    rospy.on_shutdown(cvshutdown)
    
    # launch the camera: roslaunch pi_camera camera_node.launch veh:=howard17
    # rosrun aruco_tags aruco_ros_python.py
    
