import numpy.core.multiarray
import cv2

from multiprocessing import Process, Pipe

import threading

class FaceDetect():
    def __init__(self):
        super().__init__()
        global x1
        global y1
        global x2
        global y2
        
        self.findFace()
        
    def findFace(self):
        try:
            #Load the cascade data set
            face_cascade = cv2.CascadeClassifier('cascade.xml')

            #To capture video from webcam
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            #cap.set(cv2.CAP_PROP_FPS,60)

            while True:
                #Read the frame
                _,img = cap.read()
                #_,img = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
                #convert to grayscale
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                #Detect the face
                faces = face_cascade.detectMultiScale(gray,1.1, 4)
                #Draw the rectangle around each face
                for (x, y, w, h) in faces:
                    startPoint = (x,y)
                    endPoint = (x+w, y+h)
                    cv2.rectangle(img, startPoint, endPoint, (255, 0, 0), 2)
                    #print("Start Point: ", startPoint," End Point: ", endPoint)
                    #print("X: ", x," Y: ", y, " W: ", w," H: ", h)
                    x1 = x
                    y1 = y
                    x2 = x+w
                    y2 = y+h
                    self.values(x1, y1, x2, y2)
                    #return(x, y, x+w, y+h)
                #Display
                cv2.imshow('img', img)
                
                #Passing Values through pipe
                #child_conn.send(x1, y1, x2, y2)
                #child_conn.close()
                
                #Stop if escape is pressed
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    cv2.destroyAllWindows()
                    break
        except Exception as e:
            #Release the VideoCapture object
            cap.release()
            print(e)
            #camera.close()
    
    def values(self, x1, y1, x2, y2):
        #print("Start Point: ", startPoint," End Point: ", endPoint)
        print("X1: ", x1," Y1: ", y1, " X2: ", x2," Y2: ", y2)
        
        return(x1, y1, x2, y2)
            
if __name__ == "__main__":
    #child_conn = Pipe()
    fd = FaceDetect()
