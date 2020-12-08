
import numpy as np
import cv2
import imutils
import argparse
from imutils.video import VideoStream
import time
from collections import deque


#code from Here

ap = argparse.ArgumentParser()
ap.add_argument("-v","--video",help="give the location of the video folder")
ap.add_argument("-b","--buffer",type = int,default=64,help="max buffer size")

args = vars(ap.parse_args())



if not args.get("video",False):
    vs = VideoStream(src=0).start()
else:
    vs = cv2.VideoCapture(args["video"])



while True:
    
    frame = vs.read()
    

    frame = frame[1] if args.get("video",False) else frame

    if frame is None:
        break
    

    image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    image = imutils.resize(image,width=400,height= 700)
    left = cv2.imread('Capture1.JPG')

    
    left = cv2.cvtColor(left,cv2.COLOR_BGR2GRAY)

    right = cv2.imread('Capture2.JPG')
    right = cv2.cvtColor(right,cv2.COLOR_BGR2GRAY)


    


    res = cv2.matchTemplate(image, left, cv2.TM_SQDIFF)
    res1 = cv2.matchTemplate(image, right, cv2.TM_SQDIFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

    top_left = min_loc  #Change to max_loc for all except for TM_SQDIFF
    top_left1 = min_loc1
    bottom_right = (top_left[0] + 100, top_left[1] + 75)
    bottom_right1 = (top_left1[0] + 100, top_left1[1] + 75)

    cv2.rectangle(image, top_left, bottom_right, 255, 2)  #White rectangle with thickness 2. 
    cv2.putText(image,"Capture1",top_left,cv2.FONT_HERSHEY_COMPLEX,0.3,(0,255,0))
    cv2.rectangle(image, top_left1, bottom_right1, 255, 2)
    cv2.putText(image,"Capture2",top_left1,cv2.FONT_HERSHEY_COMPLEX,0.3,(0,255,0))

    

    #Rignt Side:

    left3 = cv2.imread('Capture3.JPG')

    
    left3 = cv2.cvtColor(left3,cv2.COLOR_BGR2GRAY)

    right3 = cv2.imread('Capture4.JPG')
    right3 = cv2.cvtColor(right3,cv2.COLOR_BGR2GRAY)


    


    res3 = cv2.matchTemplate(image, left, cv2.TM_SQDIFF)
    res4 = cv2.matchTemplate(image, right, cv2.TM_SQDIFF)

    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(res3)
    min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(res4)

    top_left3 = min_loc3  #Change to max_loc for all except for TM_SQDIFF
    top_left4 = min_loc4
    bottom_right3 = (top_left3[0] + 100, top_left3[1] + 75)
    bottom_right4 = (top_left4[0] + 100, top_left4[1] + 75)

    cv2.rectangle(image, top_left3, bottom_right3, 255, 2)  #White rectangle with thickness 2. 
    cv2.putText(image,"Capture3",top_left3,cv2.FONT_HERSHEY_COMPLEX,0.3,(0,255,0))
    cv2.rectangle(image, top_left4, bottom_right4, 255, 2)
    cv2.putText(image,"Capture4",top_left4,cv2.FONT_HERSHEY_COMPLEX,0.3,(0,255,0))


    cv2.imshow("Matched image", image)
    #cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

if not args.get("video",False):
    vs.stop()
else:
    vs.release()

 
cv2.destroyAllWindows()






    


    

    
    

