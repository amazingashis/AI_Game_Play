
import numpy as np
import cv2
import imutils
import argparse
from imutils.video import VideoStream
import time

import time
from PIL import ImageGrab


#code from Here

'''
ap = argparse.ArgumentParser()
ap.add_argument("-v","--video",help="give the location of the video folder")
ap.add_argument("-b","--buffer",type =
 int,default=64,help="max buffer size")

args = vars(ap.parse_args())



if not args.get("video",False):
    vs = VideoStream(src=0).start()
else:
    vs = cv2.VideoCapture(args["video"])

frame5 = vs.read()
'''
frame5 = np.array(ImageGrab.grab(bbox=(100,109,599,988)))
#frame5 = frame5[1] if args.get("video",False) else frame
frame5 = cv2.cvtColor(frame5,cv2.COLOR_BGR2GRAY)
frame5 = imutils.resize(frame5,width=400,height= 700)
frame1 = frame5[350:350+75, 10:100]
frame2 = frame5[350:350+75, 100:200]
frame3 = frame5[350:350+75, 210:300]
frame4 = frame5[350:350+75, 300:390]


i= 0
j = 0
k=0
l=0
m = 0
n = 0
o =0
p = 0
while True:
    '''
    frame = vs.read()
    

    frame = frame[1] if args.get("video",False) else frame

    if frame is None:
        break
    '''
    image = np.array(ImageGrab.grab(bbox=(100,109,599,988)))
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = imutils.resize(image,width=400,height= 700)
    

    sub_image = image[350:350+75, 10:100]
    sub_image1 = image[350:350+75, 100:200]
    sub_image2 = image[350:350+75, 210:300]
    sub_image3 = image[350:350+75, 300:390]

    
    
    cv2.rectangle(image, (10,350), (100,425), (255,0,0), 2)  #White rectangle with thickness 2.
    cv2.rectangle(image, (100,350), (180,425), (255,0,0), 2)
    cv2.rectangle(image, (210,350), (300,425), (255,0,0), 2)
    cv2.rectangle(image, (300,350), (390,425), (255,0,0), 2)


    
    #First Box:
    diff = cv2.absdiff(sub_image,frame1)
    _, th = cv2.threshold(diff, 75, 100, cv2.THRESH_BINARY)
    cnts,hierarchy = cv2.findContours(th.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contor in cnts:
        
        
        if cv2.contourArea(contor) > 500:
            cv2.rectangle(image, (10,350), (100,425), (0,255,0), 3)
            i = i+1
          
       
    if i > 3:
        j = j+1
        print("j = ",j)
        i = 0
    
    
    
    #Second Box

    diff1 = cv2.absdiff(sub_image1,frame2)
    _, th1 = cv2.threshold(diff1, 75, 100, cv2.THRESH_BINARY)
    cnts1,hierarchy1 = cv2.findContours(th1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contorss in cnts1:
        
        
        if cv2.contourArea(contorss) > 190:
            cv2.rectangle(image, (100,350), (180,425), (0,255,0), 3)
            k = k+1
          
       
    if k > 4:
        l = l+1
        print("l = ",l)
        k = 0
    


    # Third Box

    diff2 = cv2.absdiff(sub_image2,frame3)
    _, th2 = cv2.threshold(diff2, 75, 100, cv2.THRESH_BINARY)
    cnts2,hierarchy2 = cv2.findContours(th2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contorss in cnts2:
        
        
        if cv2.contourArea(contorss) > 190:
            cv2.rectangle(image, (210,350), (300,425), (0,255,0), 3)
            m = m+1
          
       
    if m > 4:
        n = n+1
        print("n = ",n)
        m = 0
        

    #Fourth Box
    diff3 = cv2.absdiff(sub_image3,frame4)
    _, th3 = cv2.threshold(diff3, 75, 100, cv2.THRESH_BINARY)
    cnts3,hierarchy4 = cv2.findContours(th3.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contorss in cnts3:
        
        
        if cv2.contourArea(contorss) > 190:
            cv2.rectangle(image,(300,350), (390,425), (0,255,0), 3)
            o = o+1
          
       
    if o > 4:
        p = p+1
        print("p = ",p)
        o = 0
    
    cv2.imshow("Matched image", image)
    




    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

if not args.get("video",False):
    vs.stop()
else:
    vs.release()

 
cv2.destroyAllWindows()






    


    

    
    

