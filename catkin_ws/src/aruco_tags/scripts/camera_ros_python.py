#!/usr/bin/env python
# Camera bit for the simple aruco test while I don't have howard with me

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
import numpy as np
import cv2, PIL
from cv2 import aruco

def talker():
    pub = rospy.Publisher('/howard17/camera_node/image/compressed', CompressedImage, queue_size=10)
    rospy.init_node('aruco_talker')
    rate = rospy.Rate(10) # 10hz
    cap = cv2.VideoCapture('/home/jackie/duckietown/catkin_ws/src/aruco_tags/scripts/test_videos/test1.mp4')
    #cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        ret, frame = cap.read()

        if ret == True:
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame',gray)

            #rospy.loginfo(hello_str)
            #pub.publish(hello_str)
        rate.sleep()
    # Upon shutdown
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
