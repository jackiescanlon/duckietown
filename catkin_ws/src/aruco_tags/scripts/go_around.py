#!/usr/bin/env python
# Commands the duckie to turn around

import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from duckietown_msgs.msg import BoolStamped

# Runs when the lane is blocked
def control_car(data):

    global pub

    

	# Publish to the pub_tag_2 topic to be read by fsm state
	pub_tag_2.publish(b)

def  start():

    # Initialize the node
    rospy.init_node('go_around')

    # Set up the publisher
    global pub
    pub = rospy.Publisher('/howard17/obstacle_safety_node/lane_blocked', BoolStamped, queue_size=1)

    # Subscribe to the same topic 
    rospy.Subscriber('/howard17/obstacle_safety_node/lane_blocked', BoolStamped, control_car)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
	start()
    except rospy.ROSInterruptException:
	pass
