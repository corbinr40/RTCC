## Main File for RTTC

#Starts with "GUI" to show background.
#When Mic (or VA_5) is active, show mic icon
#WHen Face detect is wanted, it will call the program.
#When settings are wanted, it will call the settings page

#from tkinter import Tk, Canvas, Frame, BOTH, Menu,
import pstats
from tkinter import *
import datetime
import time

import platform

#Modules for Face Detection
#from tkinter import Tk, Canvas, Frame, BOTH
from multiprocessing import Process, Queue, Pipe
import numpy.core.multiarray
import cv2
import threading

#Current Power Level
if('linux' in platform.system().lower()):
    import smbus
else:
    pass

# BUS VOLTAGE REGISTER (R)
_REG_BUSVOLTAGE = 0x02

# CALIBRATION REGISTER (R/W) #Required
_REG_CALIBRATION = 0x05


class BusVoltageRange:
    """Constants for ``bus_voltage_range``"""
    RANGE_16V = 0x00      # set bus voltage range to 16V
    RANGE_32V = 0x01      # set bus voltage range to 32V (default)


class INA219:
    def __init__(self, i2c_bus=1, addr=0x40):
        self.bus = smbus.SMBus(i2c_bus)
        self.addr = addr

        # Set chip to known config values to start #Required
        self._cal_value = 0

    def read(self, address):
        data = self.bus.read_i2c_block_data(self.addr, address, 2)
        return ((data[0] * 256) + data[1])

    def write(self, address, data):
        temp = [0, 0]
        temp[1] = data & 0xFF
        temp[0] = (data & 0xFF00) >> 8
        self.bus.write_i2c_block_data(self.addr, address, temp)

    def set_calibration_32V_2A(self):

        #Required
        self._cal_value = 4096

        # Set Calibration register to 'Cal' calculated above #Required
        self.write(_REG_CALIBRATION, self._cal_value)

    def getBusVoltage_V(self):
        self.write(_REG_CALIBRATION, self._cal_value)
        self.read(_REG_BUSVOLTAGE)
        return (self.read(_REG_BUSVOLTAGE) >> 3) * 0.004


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
        global videoOn
        global voiceText

        #self.master.title("Face Detection")
        #self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)
        voiceText = canvas.create_text(x1, y1, fill="#ffffff", text = "")

        #canvas.configure(bg='black')
        #canvas.pack(fill=BOTH, expand=1)

        ##Menu Bar Frame
        menubarFrame = LabelFrame(root, bg="white")
        menubarFrame.pack(fill=X, expand=0)
        #menubarFrame.grid(row=0, column=0)
        
        ##Time Label
        self.currentTimeLabel = Label(menubarFrame)
        self.currentTimeLabel.pack(anchor=N, side=RIGHT)
        self.currentTime()

        ##Battery Percentage Label
        self.currentBatteryLabel = Label(menubarFrame)
        self.currentBatteryLabel.pack(anchor=E, side=RIGHT)
        self.currentPower()

        ##Recording Audio / Camera
        audioOn = canvas.create_oval(620, 460, 640, 480, fill="#F85E2B", width=2)
        videoOn = canvas.create_oval(590, 460, 610, 480, fill="#000000", width=2)

        

        self.pack(fill=BOTH, expand=1)

        root.geometry("640x480")

        #canvas = Canvas(self)

        canvas.configure(bg='black')
        canvas.pack(fill=BOTH, expand=1)

    def currentTime(self):
        time = datetime.datetime.now().strftime('%H:%M')
        self.currentTimeLabel.config(text = time)
        self.currentTimeLabel.after(1000, self.currentTime)

    def currentPower(self):
        if('linux' in platform.system().lower()):

            ina219 = INA219(addr=0x43)

            bus_voltage = ina219.getBusVoltage_V()             # voltage on V- (load side)
            p = (bus_voltage - 3)/1.2*100
            if(p > 100):
                p = 100
            if(p < 0):
                p = 0

            # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
            powerLevel = "{:3.0f}%".format(p)
            self.currentBatteryLabel.config(text= powerLevel)
            self.currentBatteryLabel.after(1000, self.currentPower)
        else:
            self.currentBatteryLabel.config(text="100%")

    #Face Detect Specific
    def createRect(self,x1, y1, x2, y2):
        global rectFace
        global canvas
        global voiceText
        canvas.delete(rectFace)
        canvas.delete(voiceText)
        #print("x1: " + str(x1) + " y1: " + str(y1) + " x2: " + str(x2) + " y2: " + str(y2))
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)
        voiceText = canvas.create_text((x2 + x1) / 2, (y2 + 25), fill="#ffffff", text="Hello")

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
                    global voiceText
                    global canvas
                    global videoOn
                    canvas.delete(rectFace)
                    canvas.delete(voiceText)
                    canvas.itemconfig(videoOn, fill='#000000')
                    pass
                else:
                    canvas.itemconfig(videoOn, fill='#89E039')
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
                        canvas.delete(voiceText)
                    
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

    def commandsList(self):
        #("640x480")
        global commandListActive
        global backgroundRec
        global commandsTitleLabel
        global speechLabel
        global visionLabel
        global settingsLabel
        global jokesLabel
        global commandsLabel
        global timeLabel
        global powerLabel
        if(commandListActive == False):
            backgroundRec = canvas.create_rectangle(10, 290, 200, 470, fill="#FFFFFF")
            commandsTitleLabel = canvas.create_text(100, 305, text='Commands')
            speechLabel = canvas.create_text(15, 330, anchor='w', text='Speech: activate speech')
            visionLabel = canvas.create_text(15, 350, anchor='w', text='Vision: activate vision')
            settingsLabel = canvas.create_text(15, 370, anchor='w', text='Settings: open settings')
            jokesLabel = canvas.create_text(15, 390, anchor='w', text='Jokes: want a joke?')
            commandsLabel = canvas.create_text(15, 410, anchor='w', text='Commands: view commands')
            timeLabel = canvas.create_text(15, 430, anchor='w', text='Time: get current time')
            powerLabel = canvas.create_text(15, 450, anchor='w', text='Power: power off device')
            commandListActive = True

            self.openCommandList()

            #time.sleep(1)
        else:
            #canvas.after(2000)

            canvas.delete(backgroundRec)
            canvas.delete(commandsTitleLabel)
            canvas.delete(speechLabel)
            canvas.delete(visionLabel)
            canvas.delete(settingsLabel)
            canvas.delete(jokesLabel)
            canvas.delete(commandsLabel)
            canvas.delete(timeLabel)
            canvas.delete(powerLabel)
            commandListActive = False

        #canvas.after(1000, self.commandsListClose())
        pass

    def openCommandList(self):
        commandThread = threading.Timer(2.0, self.commandsListClose, args=())
        commandThread.start()

    def commandsListClose(self):
        #("640x480")
        global commandListActive
        global backgroundRec
        global commandsTitleLabel
        global speechLabel
        global visionLabel
        global settingsLabel
        global jokesLabel
        global commandsLabel
        global timeLabel
        global powerLabel
        if(commandListActive == True):
            canvas.delete(backgroundRec)
            canvas.delete(commandsTitleLabel)
            canvas.delete(speechLabel)
            canvas.delete(visionLabel)
            canvas.delete(settingsLabel)
            canvas.delete(jokesLabel)
            canvas.delete(commandsLabel)
            canvas.delete(timeLabel)
            canvas.delete(powerLabel)
            commandListActive = False

        pass



    

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

#def openCommandList(ex):
#    commandThread = threading.Timer(5.0, ex.commandsListClose, args=())
##    commandThread.start()
    #commandThread.cancel()

    #while(commandThread.is_alive()):
    #    print("I'm Running!!")
    #else:
    #    ex.commandsListClose()
    #    pass

def main():
    global root
    global findFaces
    global commandListActive
    commandListActive = False
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
    root.bind("s", lambda e: print("Settings"))
    #root.bind("c", lambda e:  openCommandList(ex))
    root.bind("c", lambda e:  ex.commandsList())
    root.bind("<Escape>", lambda e: closeProgram(e))
    root.mainloop()

if __name__ == '__main__':
    main()
