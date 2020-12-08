import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from matplotlib import pyplot as plt

monk1 = 2
monk2 = 3
i = 1
while True:


    #cap = np.array(ImageGrab.grab(bbox=(100,109,593,988)))
    #image = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
    image = cv2.imread('1.jpeg')
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    left = cv2.imread('left1.JPG')
    #h, w = left.shape[::]
    
    left = cv2.cvtColor(left,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("left",left)
    right = cv2.imread('right1.JPG')
    right = cv2.cvtColor(right,cv2.COLOR_BGR2GRAY)
    #cv2.rectangle(image,(0,338),(237,538),(255,255,200),1)
    #cv2.rectangle(image,(100,352),(593,988),(255,255,200),2)

    #bbox=(100,109,593,988)
    #100,109,352,966

    '''
    ##Left arrow
    sift1 = cv2.SIFT_create()        
    kp_left1, des_left1 = sift1.detectAndCompute(left,None)
    kp_left2, des_left2 = sift1.detectAndCompute(image,None)        
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des_left1,des_left2, k=2)

    match_pts_left = []
    for m1,m2 in matches:
        if m1.distance < 0.65* m2.distance:
            idx = m1.trainIdx
            match_pts_left.append(kp_left2[idx].pt)

    if len(match_pts_left) != 0:
        match_pts_left = np.array(match_pts_left)
        #print(match_pts_left)
        #print("Left")
        cv2.putText(image,"Left",(int(match_pts_left[0, 0]), int(match_pts_left[0, 1])),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0, 255, 229),1)


    
    
    #right Arrow
    sift2 = cv2.SIFT_create()        
    kp_right1, des_right1 = sift2.detectAndCompute(right,None)
    kp_right2, des_right2 = sift2.detectAndCompute(image,None)        
    bf1 = cv2.BFMatcher()
    matches1 = bf1.knnMatch(des_right1,des_right2, k=2)

    match_pts_right = []
    for m11,m12 in matches1:
        if m11.distance < 0.65* m12.distance:
            idx1 = m11.trainIdx
            match_pts_right.append(kp_right2[idx1].pt)

    if len(match_pts_right) != 0:
        match_pts_right = np.array(match_pts_right)
        #print(match_pts_right)
        #print("Right",i)
        
        
        cv2.putText(image,"Right",(int(match_pts_right[0, 0]), int(match_pts_right[0, 1])),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0, 255, 229),1)
    
    
    
    
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



    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()