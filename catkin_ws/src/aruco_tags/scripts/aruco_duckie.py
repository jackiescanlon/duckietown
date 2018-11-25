#!/usr/bin/env python
# Simple listener that subscribes to aruco tags

import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from geometry_msgs.msg import Pose
from duckietown_msgs.msg import BoolStamped

# Runs when tag 1 is detected (tag 1 = obstacle blocking lane)
def pose(data):
    dis = data.position.z
    rospy.loginfo('Tag 1 (Obstacle blocking lane) detected.') 

    if dis > min_dist_lane:
        rospy.loginfo('Tag 1 is still far away enough: %s m', dis)
    else:
	# Set up a BoolStamped to publish
	b = BoolStamped()
	b.data = True

	# Print a message
	rospy.loginfo('Tag 1 is too close: %s m', dis)

	# Publish to the too_close topic:
	pub_too_close.publish(b)

# Runs when tag 2 is detected (tag 2 = obstacle blocking road)
def pose2(data):
    dis = data.position.z
    rospy.loginfo('Tag 2 (Obstacle blocking road) detected.') 

    if dis > min_dist_road:
        rospy.loginfo('Tag 2 is still far away enough: %s m', dis)
    else:
	# Set up a BoolStamped to publish
        b = BoolStamped()
        b.data = True
        
	# Print a message
	rospy.loginfo('Tag 2 is too close: %s m', dis)

	# Publish to the too_close topic
	pub_too_close.publish(b)

def listener():

    # Initialize the node
    rospy.init_node('aruco_duckie')
    
    # Set the distances (can evetually make this ros params?)
    global min_dist_lane
    min_dist_lane = .2
    global min_dist_road
    min_dist_road = .3
    
    # Set up the publisher
    # Currently doesn't account for the difference between tags
    global pub_too_close
    pub_too_close = rospy.Publisher('/howard17/obstacle_safety_node/object_too_close', BoolStamped, queue_size=1)
    
    # Subscribe to the nodes that give poses of tags
    rospy.Subscriber('/aruco_double/pose', Pose, pose)
    rospy.Subscriber('/aruco_double/pose2', Pose, pose2)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
	listener()
    except rospy.ROSInterruptException:
	pass
