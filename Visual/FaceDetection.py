import numpy.core.multiarray
import cv2

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
            print("Start Point: ", startPoint," End Point: ", endPoint)
            print("X: ", x," Y: ", y, " W: ", w," H: ", h)
        #Display
        cv2.imshow('img', img)
        #Stop if escape is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            cv2.destroyAllWindows()
            break
except:
    #Release the VideoCapture object
    cap.release()
    #camera.close()
