# Aruco Test from camera
import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.lines import Line2D

# Capture the camera 
cap = cv2.VideoCapture(0)

#plt.ion()
#plt.show()

# For each frame, basically of the camera input
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
            
        # Detect the Aruco tags
        
        # They come out of this dictionary, the 6x6_250
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

        # Clear the previously drawn plot
        plt.clf()

        # Plot the detections
        plt.imshow(frame_markers)
        
        # if anything was detected, plot the dots
        if ids is not None: 
            for i in range(len(ids)):
                c = corners[i][0]
                
                # Plot blue dots for id = 1
                if ids[i] == 1:
                    plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "bo") #, label = ids[i])
                # Plot yellow dots for id = 2
                elif ids[i] == 2:
                    plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "yo") #, label = ids[i])
                # Plot green dots for any other ids
                else:
                    plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "go") #, label = ids[i])
                    
        # Doesn't work without this. especially pressing q doesnt work
        # Press q a lot of times
        plt.pause(0.05)
        # Make the legend - can't get this to work rn
        #legend_entries = [Line2D([0], [0], marker='o',markerfacecolor='b', markersize=10),
                          #Line2D([0], [0], marker='o',markerfacecolor='r', markersize=10)]
        #legend_entries = [Line2D([0], [0], color='b', lw=4), Line2D([0], [0], color='r', lw=4)]
        #plt.legend(legend_entries, ['ID = 1', 'ID = 2'])
        #plt.legend()
    # Exit when someone presses q (for quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Show the plot. I have no idea why this is outside the while() but doesn't work otherwise!
plt.show()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


