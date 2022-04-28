from tkinter import Tk, Canvas, Frame, BOTH
import numpy.core.multiarray

from multiprocessing import Process, Queue, Pipe
#from FaceDetection import FaceDetect
import FaceDetection

import cv2
import threading

class Interface(Frame):

    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        
    
        self.initUI(x1, y1, x2, y2)

    def initUI(self, x1, y1, x2, y2):
        global canvas
        global rectFace
        
        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(self)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)
        
        canvas.configure(bg='black')
        canvas.pack(fill=BOTH, expand=1)
        
        #parent_conn, child_conn = Pipe()
        #self.p = Process(target=FaceDetect.findFace, args=(child_conn,))
        #self.p.start()
        #print(parent_conn.recv())
        
        #self.attributes("-fullscreen", True)
        #self.bind("<Key>", keypress)
        #self.bind("<Escape>", lambda e: closeProgram(e))

    def createRect(x1, y1, x2, y2):
        global rectFace
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)

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
    #canvas.move(rectFace, x, y)

    elif event.char == "l":
        x1 = 490
        y1 = 426
        x2 = 635
        y2 = 571

        canvas.delete(rectFace)
        Interface.createRect(x1, y1, x2, y2)


    elif event.char == "k":
        x1 = 249
        y1 = 139
        x2 = 403
        y2 = 293

        canvas.delete(rectFace)
        Interface.createRect(x1, y1, x2, y2)
        #rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)
    
def closeProgram(e):
    root.destroy()

def main():
    #global x1
    #global y1
    #global x2
    #global y2
    global root
    
    #FaceDetection.values()
    
    x1 = 100
    y1 = 100
    x2 = 200
    y2 = 200
    
    root = Tk()
    
    ex = Interface(x1, y1, x2, y2)
    
    #root.wm_attributes("-topmost", True)
    root.attributes("-fullscreen", True)
    
    root.bind("<Key>", keypress)
    root.bind("<Escape>", lambda e: closeProgram(e))
    root.mainloop()
    
    

if __name__ == '__main__':
    main()
