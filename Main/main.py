## Main File for RTTC

#Starts with "GUI" to show background.
#When Mic (or VA_5) is active, show mic icon
#WHen Face detect is wanted, it will call the program.
#When settings are wanted, it will call the settings page

#from tkinter import Tk, Canvas, Frame, BOTH, Menu,
from tkinter import *
import datetime

class Interface(Frame):

    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.master.title("RTTC")

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

        canvas = Canvas(self)

        canvas.configure(bg='black')
        canvas.pack(fill=BOTH, expand=1)

    def currentTime(self):
        time = datetime.datetime.now().strftime('%H:%M')
        self.currentTimeLabel.config(text = time)
        self.currentTimeLabel.after(1000, self.currentTime)

def donothing():
        x = 0
    

def closeProgram(e):
    root.destroy()


def main():
    global root

    root = Tk()

    ex = Interface()

    #root.wm_attributes("-topmost", True)
    root.attributes("-fullscreen", True)

    root.bind("<Escape>", lambda e: closeProgram(e))
    root.mainloop()

if __name__ == '__main__':
    main()
