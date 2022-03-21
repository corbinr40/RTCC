from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)
        
        global canvas
        global rectFace

        canvas = Canvas(self)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2,
            outline="#f11", width=2)
        
        canvas.configure(bg='black')
        canvas.pack(fill=BOTH, expand=1)

def keypress(event):
    x, y = 0, 0
    if event.char == "a": 
        #print('"a" Pressed')
        x = -10
    elif event.char == "d": 
        #print('"d" Pressed')
        x = 10
    elif event.char == "w": 
        #print('"w" Pressed')
        y = -10
    elif event.char == "s": 
        #print('"s" Pressed')
        y = 10
    canvas.move(rectFace, x, y)
    
def closeProgram(e):
    root.destroy()

def main():
    global x1
    global y1
    global x2
    global y2
    
    x1 = 490
    y1 = 426
    x2 = 635
    y2 = 571
    
    global root
    root = Tk()
    ex = Example()
    #root.geometry("330x220+300+300")
    #root.geometry("1280x720")
    root.wm_attributes("-topmost", True)
    #root.wm_attributes("-disabled", True)
    #root.wm_attributes("-transparentcolor", "white")
    #root.wm_attributes("-alpha", 0.5)
    #root.configure(bg='red')
    #root['bg'] = 'green'
    root.attributes("-fullscreen", True)
    
    root.bind("<Key>", keypress)
    root.bind("<Escape>", lambda e: closeProgram(e))
    root.mainloop()


if __name__ == '__main__':
    main()
