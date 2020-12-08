
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
    
    #image = cv2.imread('1.jpeg')
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    image = imutils.resize(image,width=400,height= 700)
    left = cv2.imread('left1.JPG')
    #h, w = left.shape[::]
    
    left = cv2.cvtColor(left,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("left",left)
    right = cv2.imread('right1.JPG')
    right = cv2.cvtColor(right,cv2.COLOR_BGR2GRAY)
    '''
    frame = cv2.imread('1.jpeg')
    frame = imutils.resize(frame,width=400,height= 700)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    edged = cv2.Canny(blur,150,160)
    cv2.imshow("blurred", edged)
    contour = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(contour)

    count = None

    if len(cnts) >0:
        #cnts = sorted(cnts,key= cv2.contourArea,reverse=True)
        for c in cnts:
            peri = cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,0.09*peri,True)

            if len(approx) == 4:
                #count.append(approx)
                count = approx
                break

    #print(len(c))
    for c in count:

        cv2.drawContours(frame,[c],-1,(0,255,0),2)

    


    '''
    res = cv2.matchTemplate(image, left, cv2.TM_SQDIFF)
    res1 = cv2.matchTemplate(image, right, cv2.TM_SQDIFF)
    #plt.imshow(res, cmap='gray')
    
    #cv2.imshow(res, cmap='gray')
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

    top_left = min_loc  #Change to max_loc for all except for TM_SQDIFF
    top_left1 = min_loc1
    bottom_right = (top_left[0] + 100, top_left[1] + 75)
    bottom_right1 = (top_left1[0] + 100, top_left1[1] + 75)

    cv2.rectangle(image, top_left, bottom_right, 255, 2)  #White rectangle with thickness 2. 
    cv2.rectangle(image, top_left1, bottom_right1, 255, 2)

    cv2.imshow("Matched image", image)

    #cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

if not args.get("video",False):
    vs.stop()
else:
    vs.release()

 
cv2.destroyAllWindows()






    


    

    
    

