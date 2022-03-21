from tkinter import Tk, Canvas, Frame, BOTH
import numpy.core.multiarray
import cv2

class Example(Frame):

    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        global canvas
        global rectFace
        
        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(self)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2,
            outline="#f11", width=2)
        
        canvas.configure(bg='black')
        canvas.pack(fill=BOTH, expand=1)

def keypress(event):
    x, y = 0, 0
    if event.char == "a": 
        x = -10
    elif event.char == "d": 
        x = 10
    elif event.char == "w": 
        y = -10
    elif event.char == "s": 
        y = 10
    canvas.move(rectFace, x, y)
    
def closeProgram(e):
    root.destroy()

def main():
    global x1
    global y1
    global x2
    global y2
    global root
    
    x1 = 490
    y1 = 426
    x2 = 635
    y2 = 571
    
    root = Tk()
    ex = Example()
    #root.wm_attributes("-topmost", True)
    root.attributes("-fullscreen", True)
    
    root.bind("<Key>", keypress)
    root.bind("<Escape>", lambda e: closeProgram(e))
    root.mainloop()
    
    try:
        face_cascade = cv2.CascadeClassifier('cascade.xml')

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

        while True:
            _,img = cap.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.1, 4)
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
        cap.release()

if __name__ == '__main__':
    main()
    
    
    




