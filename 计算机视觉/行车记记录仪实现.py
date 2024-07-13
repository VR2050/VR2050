import cv2
import numpy as np 
import time
capture=cv2.VideoCapture(0)
if capture.isOpened () is False:
    print("error")
    exit(-1)
    
width=int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth=int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


fps=capture.get(cv2.CAP_PROP_FPS)

tim=int(input("Please input your time"))
fourcc=cv2.VideoWriter_fourcc(*'mp4v')

out=cv2.VideoWriter("/root/video/out-"+str(0)+".mp4",fourcc,fps,(width,heigth))
start=time.time()
file_num=1
while cv2.waitKey(2) & 0xFF !=ord('q'):
    if time.time()-start>=tim:
        out.release()
        file_num+=1
        out=cv2.VideoWriter("/root/video/out-"+str(file_num)+".mp4",fourcc,fps,(width,heigth))
        start=time.time()
    
    ret,frame=capture.read()
    if ret==True:
        out.write(frame)
        cv2.imshow("camera",frame)
    else:
        break
out.release()
capture.release()
cv2.destroyAllWindows()
    
