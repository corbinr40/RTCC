## Main File for RTTC

#Starts with "GUI" to show background.
#When Mic (or VA_5) is active, show mic icon
#WHen Face detect is wanted, it will call the program.
#When settings are wanted, it will call the settings page

#from tkinter import Tk, Canvas, Frame, BOTH, Menu,
from tkinter import *
import datetime

#Modules for Face Detection
#from tkinter import Tk, Canvas, Frame, BOTH
from multiprocessing import Process, Queue, Pipe
import numpy.core.multiarray
import cv2
import threading

class Interface(Frame):

    def __init__(self, x1, y1, x2, y2):
        super().__init__()

        #Face Detection Specific
        
        thread = threading.Thread(target=self.findFace, args=())
        thread.daemon = True
        thread.start()
        
        self.initUI(x1, y1, x2, y2)

    def initUI(self, x1, y1, x2, y2):
        self.master.title("RTTC")

        #Face Detection Specific
        global canvas
        global rectFace

        #self.master.title("Face Detection")
        #self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)

        #canvas.configure(bg='black')
        #canvas.pack(fill=BOTH, expand=1)

        ##Time Label
        self.currentTimeLabel = Label(root)
        self.currentTimeLabel.pack()
        self.currentTime()

        self.pack(fill=BOTH, expand=1)

        ##Test menu bar
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        batteryMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='BatteryLevel', menu=batteryMenu)
        ##

        menubarFrame = LabelFrame(root, text="Menu Bar", bg="white")
        menubarFrame.pack()
        #menubarFrame.grid(row=0, column=0)

        
        
        root.config(menu=menubar)

        #canvas = Canvas(self)

        canvas.configure(bg='black')
        canvas.pack(fill=BOTH, expand=1)

    def currentTime(self):
        time = datetime.datetime.now().strftime('%H:%M')
        self.currentTimeLabel.config(text = time)
        self.currentTimeLabel.after(1000, self.currentTime)

    #Face Detect Specific
    def createRect(self,x1, y1, x2, y2):
        global rectFace
        global canvas
        canvas.delete(rectFace)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)

    def findFace(self):
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

    

def donothing():
        x = 0
    

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
