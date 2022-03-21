from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys

import cv2

#X = 490
#Y = 426
#W = 163
#H = 163

X = 0
Y = 0
W = 0
H = 0

# It is considered a good tone to name classes in CamelCase.
class MyFirstGUI(QMainWindow): 

    def __init__(self):
        # Initializing QDialog and locking the size at a certain value
        super(MyFirstGUI, self).__init__()
        self.setWindowTitle("Face Location")
        self.setFixedSize(1280, 720)
        #self.setWindowOpacity(0.1)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, e):
        # Draw Rectangle
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        #painter.drawRect(490, 426, 635, 571)
        #painter.drawRect(490, 426, 163, 163)
        painter.drawRect(X, Y, W, H)




try:
    if __name__ == '__main__':
        #Load the cascade data set
        face_cascade = cv2.CascadeClassifier('cascade.xml')

        #To capture video from webcam
        cap = cv2.VideoCapture(0)

        app = QApplication(sys.argv)
        gui = MyFirstGUI()
        
        



        while True:
            #Read the frame
            _,img = cap.read()
            #convert to grayscale
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #Detect the face
            faces = face_cascade.detectMultiScale(gray,1.1, 4)
            #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                startPoint = (x,y)
                endPoint = (x+w, y+h)
                X = x
                Y = y
                W = w
                H = h
                cv2.rectangle(img, startPoint, endPoint, (255, 0, 0), 2)
                print("Start Point: ", startPoint," End Point: ", endPoint)
                print("X: ", x," Y: ", y, " W: ", w," H: ", h)
                #gui.update()
                gui.show()

                sys.exit(app.exec_())
except:
    #Release the VideoCapture object
    cap.release()