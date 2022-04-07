from tkinter import Tk, Canvas, Frame, BOTH
from multiprocessing import Process, Queue, Pipe
import numpy.core.multiarray
import cv2
import threading



class Interface(Frame):

    def __init__(self, x1, y1, x2, y2):
        super().__init__()

        thread = threading.Thread(target=self.findFace, args=())
        thread.daemon = True
        thread.start()
        
        self.initUI(x1, y1, x2, y2)

    def initUI(self, x1, y1, x2, y2):
        global canvas
        global rectFace
        global findFaces

        self.master.title("Face Detection")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)

        canvas.configure(bg='black')
        canvas.pack(fill=BOTH, expand=1)

    def createRect(self,x1, y1, x2, y2):
        global rectFace
        global canvas
        global findFaces
        canvas.delete(rectFace)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)

    def findFace(self):
        global findFaces
        try:
            #Load the cascade data set
            face_cascade = cv2.CascadeClassifier('cascade.xml')

            #To capture video from webcam
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            #cap.set(cv2.CAP_PROP_FPS,60)

            while True:
                #Read the frame
                _, img = cap.read()
                #convert to grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #Detect the face
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                #Draw the rectangle around each face
                foundFace = False
                #findFaces = False
                if(findFaces == False):
                    global rectFace
                    global canvas
                    canvas.delete(rectFace)
                    pass
                else:
                    for (x, y, w, h) in faces:
                        startPoint = (x, y)
                        endPoint = (x + w, y + h)
                        cv2.rectangle(img, startPoint, endPoint, (255, 0, 0), 2)
                        x1 = x
                        y1 = y
                        x2 = x + w
                        y2 = y + h
                        foundFace = True
                        self.values(x1, y1, x2, y2)
                    if(foundFace == False):
##                        global rectFace
##                        global canvas
                        canvas.delete(rectFace)
                    
                    
                #Display
                #cv2.imshow('img', img)

                #Stop if escape is pressed
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    cv2.destroyAllWindows()
                    break
        except Exception as e:
            #Release the VideoCapture object
            cap.release()
            print(e)
            #camera.close()

    def values(self, x1, y1, x2, y2):
        #print("X1: ", x1, " Y1: ", y1, " X2: ", x2, " Y2: ", y2)

        self.createRect(x1, y1, x2, y2)
        return (x1, y1, x2, y2)

def closeProgram(e):
    root.destroy()

def pauseFaceDect(e):
    global findFaces
    if(findFaces == False):
        findFaces = True
        print("findFaces is True")
    else:
        findFaces = False
        print("findFaces is False")


def main():
    global root
    global findFaces
    findFaces = False

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    root = Tk()

    ex = Interface(x1, y1, x2, y2)

    #root.wm_attributes("-topmost", True)
    root.attributes("-fullscreen", True)

    root.bind("o", lambda e: pauseFaceDect(e))
    root.bind("<Escape>", lambda e: closeProgram(e))
    root.mainloop()

if __name__ == '__main__':
    main()
