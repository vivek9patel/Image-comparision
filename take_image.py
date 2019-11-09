'''import time
from  import Camera

cam = Camera()
time.sleep(0.1)  # If you don't wait, the image will be dark
img = cam.getImage()
img.save("simplecv.png")'''
import time
import cv2
try:
    while True:
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("NewPicture.jpg",frame)
            result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()

            time.sleep(60)
            #cv2.imshow('img',img)
            #if cv2.waitKey(0) & 0xFF == ord('q'):
            #   break
except KeyboardInterrupt:
    # Close the window 
    cap.release() 

    # De-allocate any associated memory usage 
    cv2.destroyAllWindows()




