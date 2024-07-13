import cv2
import  time
capture=cv2.VideoCapture(0) 
if capture.isOpened()==False:
    print("error")
    exit(-1)
print(capture.get(cv2.CAP_PROP_FPS))
while True:
    ret,frame=capture.read()
    cv2.imshow("camera",frame)  
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    time.sleep(0.1)
    
capture.release()
cv2.destroyAllWindows()