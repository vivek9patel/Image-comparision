# Python program to illustrate 
# template matching 
import cv2 
import numpy as np
import math
import time
while True:
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("detected.jpg",frame)
        result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()
        flag = 0
        total_occupancy=12
# Read the main image
#Rename image before using it
        img_rgb = cv2.imread('mario.jpg')

        img = np.full((100,80,3), 12, np.uint8)

# Convert it to grayscale 
        img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY) 

# Read the template
#Enter any template image you want to find in camers's image
        template = cv2.imread('mario_coin.jpg',0) 

# Store width and heigth of template in w and h 
        w, h = template.shape[::-1] 

# Perform match operations. 
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 

# Specify a threshold 
        threshold = 0.8

# Store the coordinates of matched area in a numpy array 
        loc = np.where( res >= threshold)
        count = 0
        last_pt = [0, 0]

# Draw a rectangle around the matched region.
#print(flag)
        for pt in sorted(zip(*loc[::-1])):
            flag = flag+1
                #print(flag)
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
            if math.sqrt(abs(last_pt[0]-pt[0])**2 + abs(last_pt[0]-pt[0])**2) < threshold*min([h, w]):
                    continue
            else:
                last_pt = pt
                    #print(pt)
                
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                #count = count + 1

# Show the final image with the matched area. 
            cv2.imshow('LIVE',img_rgb)
#vacant_seat=total_occupancy - flag
        print("Number of templates are found  : " , int(count))

       
            #f = open('file.txt', 'r+')
            #f.truncate(0) # need '0' when using r+
        with open("output.txt", "a") as f:
            f.truncate(0) # need '0' when using r+
            print("Number of templates are found  : " , int(count), file=f)  
            time.sleep(5)

    if cv2.waitKey(1)== 27 :
        break
        
        
    cv2.destroyAllWindows()

            #cv2.imshow('img',img)
            #if cv2.waitKey(0) & 0xFF == ord('q'):
            #   break
