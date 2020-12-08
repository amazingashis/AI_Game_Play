
import pyautogui
print(pyautogui.position())







ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="the path of the image file")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
#cv2.imshow("image",image)
#image = imutils.resize(image,width=500,height)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray",gray)
blur = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(blur,75,200)
#cv2.imshow("edged",edged)
contour = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contour)

count = None

if len(cnts) >0:
    cnts = sorted(cnts,key= cv2.contourArea,reverse=True)
    for c in cnts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*peri,True)

        if len(approx) ==4:
            #count.append(approx)
            count = approx
            break

'''         
print(len(c))
for c in count:
    cv2.drawContours(image,[c],-1,(0,255,0),2)
'''
#plate = four_point_transform(image,count.reshape(4,2))
cv2.drawContours(image,[count],-1,(0,255,0),2)
fplate = four_point_transform(gray,count.reshape(4,2))


text = pytesseract.image_to_string(fplate,config='--psm 11')
#print(text)
text = text.strip()
text = text.replace(" ","")
text = str.join(" ", text.splitlines())

text = "The number plate is ::" + text
print(text)
cv2.putText(image,text,(20,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255),2)
cv2.imshow("plate",image)
cv2.waitKey(0)


cv2.destroyAllWindows()



