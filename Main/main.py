## Main File for RTTC

#Starts with "GUI" to show background.
#When Mic (or VA_5) is active, show mic icon
#When Face detect is wanted, it will call the program.
#When settings are wanted, it will call the settings page

##Main Gui Interface Modules
import pstats
from statistics import mode
from tkinter import *
import datetime
import time
import platform

##Fault Handling
if('windows' in platform.system().lower()):
    pass
else:
    import faulthandler; faulthandler.enable()

#################################

#Modules for Face Detection
from multiprocessing import Process, Queue, Pipe
import numpy.core.multiarray
import cv2
import threading

#################################

##Settings Interface
import configparser
from numpy import column_stack, size

global fontSize
global fontColour
global wakeWord
global command
command = ''

config = configparser.ConfigParser()
config.read('settings.ini')
fontSize = config['USER SETTINGS']['fontSize']
fontColour = config['USER SETTINGS']['fontColour']
wakeWord = config['USER SETTINGS']['wakeWord']
modelSize = config['USER SETTINGS']['model']

#################################

##Voice Detection Component
## Speech to text for further development
#import pyttsx3
import pyjokes
import re
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import sys

q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

device_info = sd.query_devices(0, 'input')
samplerate = int(device_info['default_samplerate'])

if(modelSize == "large"):
    model = Model("modelLarge")
elif(modelSize == "small"):
    model = Model("modelSmall")
else:
    model = Model("modelSmall")

#################################

#Current Power Level
if('linux' in platform.system().lower()):
    import smbus
else:
    pass

# BUS VOLTAGE REGISTER (R)
_REG_BUSVOLTAGE = 0x02

# CALIBRATION REGISTER (R/W)
_REG_CALIBRATION = 0x05


class BusVoltageRange:
    """Constants for ``bus_voltage_range``"""
    RANGE_16V = 0x00      # set bus voltage range to 16V
    RANGE_32V = 0x01      # set bus voltage range to 32V (default)


class INA219:
    def __init__(self, i2c_bus=1, addr=0x40):
        self.bus = smbus.SMBus(i2c_bus)
        self.addr = addr

        # Set chip to known config values to start
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
        self._cal_value = 4096

        # Set Calibration register to 'Cal' calculated above
        self.write(_REG_CALIBRATION, self._cal_value)

    def getBusVoltage_V(self):
        self.write(_REG_CALIBRATION, self._cal_value)
        self.read(_REG_BUSVOLTAGE)
        return (self.read(_REG_BUSVOLTAGE) >> 3) * 0.004


class Interface(Frame):

    def __init__(self, x1, y1, x2, y2):
        super().__init__()

        #Face Detection Specific
        visualThread = threading.Thread(target=self.findFace, args=())
        visualThread.daemon = True
        visualThread.start()

        #Voice Detection Specific
        audioThread = threading.Thread(target=self.detectVoice, args=())
        audioThread.daemon = True
        audioThread.start()

        self.initUI(x1, y1, x2, y2)

    def initUI(self, x1, y1, x2, y2):
        self.master.title("RTTC")

        #Face Detection Specific
        global canvas
        global rectFace
        global videoOn
        global voiceText
        global audioOn

        #self.master.title("Face Detection")
        #self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.grid()
        rectFace = self.canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)
        voiceText = self.canvas.create_text(x1, y1, fill="#ffffff", text = "")

        ##Menu Bar Frame
        menubarFrame = LabelFrame(root, bg="white")
        menubarFrame.pack(fill=X, expand=0)
        
        ##Time Label
        self.currentTimeLabel = Label(menubarFrame)
        self.currentTimeLabel.pack(anchor=N, side=RIGHT)
        self.currentTime()

        ##Battery Percentage Label
        self.currentBatteryLabel = Label(menubarFrame)
        self.currentBatteryLabel.pack(anchor=E, side=RIGHT)
        self.currentPower()

        ##Recording Audio / Camera
        audioOn = self.canvas.create_oval(620, 460, 640, 480, fill="#000000", width=2)
        videoOn = self.canvas.create_oval(590, 460, 610, 480, fill="#000000", width=2)

        

        self.pack(fill=BOTH, expand=1)

        #root.geometry("640x480")

        root.geometry("650x520")

        self.canvas.configure(bg='black')
        self.canvas.pack(fill=BOTH, expand=1)

    def currentTime(self):
        time = datetime.datetime.now().strftime('%H:%M')
        self.currentTimeLabel.config(text = time)
        self.currentTimeLabel.after(1000, self.currentTime)

    def currentPower(self):
        if('linux' in platform.system().lower()):

            ina219 = INA219(addr=0x43)

            bus_voltage = ina219.getBusVoltage_V()
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
            self.currentBatteryLabel.config(text="N/A")

    #Face Detect Specific
    def createRect(self,x1, y1, x2, y2):
        global rectFace
        global canvas
        global voiceText
        global fontColour
        global command
        global audioCheck
        self.canvas.delete(rectFace)
        self.canvas.delete(voiceText)
        rectFace = self.canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)

        if(audioCheck == False):
            global canvas
            global audioOn
            self.canvas.itemconfig(audioOn, fill='#000000')
            voiceText = self.canvas.create_text((x2 + x1) / 2, (y2 + 25), fill=fontColour, font=('', fontSize), text="")
            pass
        else:
            self.canvas.itemconfig(audioOn, fill='#F85E2B')
            voiceText = self.canvas.create_text((x2 + x1) / 2, (y2 + 25), fill=fontColour, font=('', fontSize), text=command)

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
                    self.canvas.delete(rectFace)
                    self.canvas.delete(voiceText)
                    self.canvas.itemconfig(videoOn, fill='#000000')
                    pass
                else:
                    self.canvas.itemconfig(videoOn, fill='#89E039')
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
                        self.canvas.delete(rectFace)
                        self.canvas.delete(voiceText)

                #Stop if escape is pressed
                k = cv2.waitKey(30) & 0xff
                if(k == 27):
                    cv2.destroyAllWindows()
                    break
        except Exception as e:
            #Release the VideoCapture object
            cap.release()
            print(e)

    def values(self, x1, y1, x2, y2):
        self.createRect(x1, y1, x2, y2)
        return (x1, y1, x2, y2)

    def detectVoice(self):
        global audioCheck
        global command
        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=0, dtype='int16', channels=1, callback=callback):
            rec = KaldiRecognizer(model, samplerate)
            while True:
                try:
                    data = q.get()
                    if rec.AcceptWaveform(data):
                        phrase = str(rec.Result()).replace('{', '').replace('}', '').replace('text', '').replace('"', '').replace(':', '')
                        if('armadillo' in phrase):
                            phrase = phrase.replace('armadillo','')
                            self.executeCommand(phrase.lower())
                        else:
                            command = str(rec.Result()).replace('{', '').replace('}', '').replace('text', '').replace('"', '').replace(':', '')
                    else:
                        command = str(rec.PartialResult()).replace('{', '').replace('}', '').replace('partial', '').replace('"', '').replace(':', '')
                except Exception as e:
                    print(e)
                    self.notificationShow("No Microphone Detected")
                    pass

    def executeCommand(self, command):
        print(command)
        if('joke' in command):
            joke = pyjokes.get_joke()
            self.notificationShow(joke)
            print(joke)
        elif('setting' in command):
            settingsThread = threading.Thread(
                target=settingsStart(), args=())
            settingsThread.daemon = True
            settingsThread.start()
            print("Settings open")
            pass
        elif('size' in command):
            if('increase' in command):
                fontSizeIncrease()
                self.notificationShow('Font size increased')
                pass
            elif('decrease' in command):
                fontSizeDecrease()
                self.notificationShow('Font size decreased')
                pass
        elif('colour' in command):
            print(command)
            colours = ['red', 'blue', 'green', 'white']
            if(any(r in command for r in colours)):
                if('red' in command):
                    fontColourRed()
                    self.notificationShow('Font colour set to red')
                    pass
                elif('blue' in command):
                    fontColourBlue()
                    self.notificationShow('Font colour set to blue')
                    pass
                elif('green' in command):
                    fontColourGreen()
                    self.notificationShow('Font colour set to green')
                    pass
                elif('white' in command):
                    fontColourWhite()
                    self.notificationShow('Font colour set to white')
                    pass
                pass
            else:
                self.notificationShow('Colour not supported')
                print("Not Found")
        elif('conversation' and 'start' in command):
            output = command.replace('conversation', '').replace('start', '')
            pauseAudioDect()
            self.notificationShow('Starting audio detection')
        elif('conversation' and 'stop' in command):
            output = "conversation finished"
            pauseAudioDect()
            self.notificationShow('Ending audio detection')
        elif('face' and 'detection' in command):
            pauseFaceDect()
            self.notificationShow('Toggled face detection')
            pass
        elif('command' in command):
            self.commandsList()
            self.notificationShow('Showing command list')
            pass
        elif('power' and 'down' in command):
            print("Goodbye")
            closeProgram()
            quit()
        else:
            print("Not a command")
            print('Please repeate that command')
            self.notificationShow('Command not found')

    def commandsList(self):
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
            global fontColour
            if(fontColour == 'white'):
                fontColour = 'black'

            backgroundRec = self.canvas.create_rectangle(10, 290, 300, 470, fill="#FFFFFF")
            commandsTitleLabel = self.canvas.create_text(100, 305, fill=fontColour, font=('', fontSize), text='Commands')
            speechLabel = self.canvas.create_text(15, 330, anchor='w', fill=fontColour, font=('', (int(fontSize))), text='Speech: activate speech')
            visionLabel = self.canvas.create_text(15, 350, anchor='w', fill=fontColour, font=('', fontSize), text='Vision: activate vision')
            settingsLabel = self.canvas.create_text(15, 370, anchor='w', fill=fontColour, font=('', fontSize), text='Settings: open settings')
            jokesLabel = self.canvas.create_text(15, 390, anchor='w', fill=fontColour, font=('', fontSize), text='Jokes: want a joke?')
            commandsLabel = self.canvas.create_text(15, 410, anchor='w', fill=fontColour, font=('', fontSize), text='Commands: view commands')
            timeLabel = self.canvas.create_text(15, 430, anchor='w', fill=fontColour, font=('', fontSize), text='Time: get current time')
            powerLabel = self.canvas.create_text(15, 450, anchor='w', fill=fontColour, font=('', fontSize), text='Power: power off device')
            commandListActive = True

            if(fontColour == 'black'):
                fontColour = 'white'

            self.openCommandList()

    def openCommandList(self):
        commandThread = threading.Timer(2.0, self.commandsListClose, args=())
        commandThread.start()

    def commandsListClose(self):
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
            self.canvas.delete(backgroundRec)
            self.canvas.delete(commandsTitleLabel)
            self.canvas.delete(speechLabel)
            self.canvas.delete(visionLabel)
            self.canvas.delete(settingsLabel)
            self.canvas.delete(jokesLabel)
            self.canvas.delete(commandsLabel)
            self.canvas.delete(timeLabel)
            self.canvas.delete(powerLabel)
            commandListActive = False

        pass

    def notificationShow(self, commandOutput):
        global notifListActive
        global backgroundNotifRec
        global notifLabel

        if(notifListActive == False):
            global fontColour
            if(fontColour == 'white'):
                fontColour = 'black'
            backgroundNotifRec = self.canvas.create_rectangle(
                345, 400, 635, 450, fill="#FFFFFF")
            notifLabel = self.canvas.create_text(
                500, 425, fill=fontColour, font=('', fontSize), text=commandOutput)
            notifListActive = True

            if(fontColour == 'black'):
                fontColour = 'white'

            self.openNotification()
        else:
            self.canvas.delete(backgroundNotifRec)
            self.canvas.delete(notifLabel)
            notifListActive = False

        pass

    def openNotification(self):
        notificationThread = threading.Timer(2.0, self.notificationClose, args=())
        notificationThread.start()

    def notificationClose(self):
        global notifListActive
        global backgroundNotifRec
        global notifLabel
        if(notifListActive == True):
            self.canvas.delete(backgroundNotifRec)
            self.canvas.delete(notifLabel)
            notifListActive = False
        pass


def closeProgram():
    root.destroy()

def pauseFaceDect():
    global findFaces
    if(findFaces == False):
        findFaces = True
        print("findFaces is True")
    else:
        findFaces = False
        print("findFaces is False")


def pauseAudioDect():
    global audioCheck
    if(audioCheck == False):
        audioCheck = True
        print("audioCheck is True")
    else:
        audioCheck = False
        print("audioCheck is False")

def main():
    global root
    global findFaces
    global audioCheck
    global commandListActive
    global notifListActive
    commandListActive = False
    notifListActive = False
    findFaces = False
    audioCheck = False
    
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    root = Tk()

    ex = Interface(x1, y1, x2, y2)
    root.attributes("-fullscreen", True)

    root.bind("o", lambda e: pauseFaceDect())
    root.bind("p", lambda e: pauseAudioDect())
    root.bind("s", lambda e: settingsStart())
    root.bind("c", lambda e:  ex.commandsList())
    root.bind("<Escape>", lambda e: closeProgram())
    root.bind("f", lambda e: ex.notificationShow('Notfication Check'))
    root.mainloop()


## Settings Window components
class Settings():

    def __init__(sett, window):

        sett.window = window

        window.title("Settings")
        window.resizable(False, False)

        window_height = 700
        window_width = 500

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        window.geometry("{}x{}+{}+{}".format(window_width,window_height, x_cordinate, y_cordinate))

        frame = Frame(sett.window)
        frame.grid(row=0, column=0)

        global fontColour
        if(fontColour == 'white'):
            fontColour = 'black'

        sett.settingsTitleLabel = Label(frame, text='Settings', font=(
            '', (int(fontSize) * (2))), fg=fontColour)
        sett.settingsTitleLabel.grid(row=0, column=1, columnspan=2)

        sett.fontSizeLabel = Label(
            frame, text='Font Size:', font=('', fontSize), fg=fontColour)
        sett.fontSizeLabel.grid(row=1, column=0)

        sett.currentFontSizeLabel = Label(
            frame, text=fontSize, font=('', fontSize), fg=fontColour)
        sett.currentFontSizeLabel.grid(row=1, column=1)

        sett.fontColourLabel = Label(
            frame, text='Font Colour:', font=('', fontSize), fg=fontColour)
        sett.fontColourLabel.grid(row=2, column=0)

        sett.currentFontColourLabel = Label(
            frame, text=fontColour, font=('', fontSize), fg=fontColour)
        sett.currentFontColourLabel.grid(row=2, column=1)

        sett.wakeWordLabel = Label(
            frame, text='Wake Word:', font=('', fontSize), fg=fontColour)
        sett.wakeWordLabel.grid(row=3, column=0)

        sett.currentWakeWordLabel = Label(
            frame, text=wakeWord, font=('', fontSize), fg=fontColour)
        sett.currentWakeWordLabel.grid(row=3, column=1)

        sett.powerLabel = Label(frame, text='Power',
                                font=('', fontSize), fg=fontColour)
        sett.powerLabel.grid(row=4, column=0)

        sett.closeLabel = Label(frame, text='Close',
                                font=('', fontSize), fg=fontColour)
        sett.closeLabel.grid(row=5, column=0)

        if(fontColour == 'black'):
            fontColour = 'white'

        #sett.grid()

    def fontColourBlue(sett, window):
        print("Shift I pressed for Blue")
        global fontColour
        fontColour = 'blue'
        sett.currentFontColourLabel.config(text=fontColour)
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        sett.refresh(window)
        pass

    def fontColourRed(sett, window):
        print("Shift P pressed for Red")
        global fontColour
        fontColour = 'red'
        sett.currentFontColourLabel.config(text=fontColour)
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        sett.refresh(window)
        pass

    def fontColourGreen(sett, window):
        print("Shift O pressed for Green")
        global fontColour
        fontColour = 'green'
        sett.currentFontColourLabel.config(text=fontColour)
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        sett.refresh(window)
        pass

    def fontColourWhite(sett, window):
        print("Shift U pressed for white")
        global fontColour
        fontColour = 'white'
        sett.currentFontColourLabel.config(text=fontColour)
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        sett.refresh(window)
        pass

    def fontSizeIncrease(sett, window):
        global fontSize
        if(int(fontSize) <= 38):
            fontSize = int(fontSize) + 2
            config.set('USER SETTINGS', 'fontSize', str(fontSize))
            sett.refresh(window)
            pass
        pass

    def fontSizeDecrease(sett, window):
        global fontSize
        if(int(fontSize) >= 10):
            fontSize = int(fontSize) - 2
            config.set('USER SETTINGS', 'fontSize', str(fontSize))
            sett.refresh(window)
            pass
        pass

    def refresh(sett, window):
        sett.window.destroy()
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        settingsStart()


def fontColourBlue():
    print("Font Colour Blue")
    global fontColour
    fontColour = 'blue'
    config.set('USER SETTINGS', 'fontColour', str(fontColour))
    pass

def fontColourRed():
    print("Font Colour Red")
    global fontColour
    fontColour = 'red'
    config.set('USER SETTINGS', 'fontColour', str(fontColour))
    pass

def fontColourGreen():
    print("Font Colour Green")
    global fontColour
    fontColour = 'green'
    config.set('USER SETTINGS', 'fontColour', str(fontColour))
    pass

def fontColourWhite():
    print("Font Colour white")
    global fontColour
    fontColour = 'white'
    config.set('USER SETTINGS', 'fontColour', str(fontColour))
    pass

def fontSizeIncrease():
    global fontSize
    if(int(fontSize) <= 38):
        fontSize = int(fontSize) + 2
        config.set('USER SETTINGS', 'fontSize', str(fontSize))
        pass
    pass

def fontSizeDecrease():
    global fontSize
    if(int(fontSize) >= 10):
        fontSize = int(fontSize) - 2
        config.set('USER SETTINGS', 'fontSize', str(fontSize))
        pass
    pass

def settingsCloseProgram(e):
    window.destroy()

def settingsStart():
    global window
    global fontSize
    global fontColour
    global wakeWord
    window = Tk()

    settwin = Settings(window)

    if('linux' in platform.system().lower()):
        window.wm_attributes('-type', 'splash')
    else:
        pass

    window.bind("<Escape>", lambda e: settingsCloseProgram(e))
    window.bind("<P>", lambda e: settwin.fontColourRed(window))
    window.bind("<O>", lambda e: settwin.fontColourGreen(window))
    window.bind("<I>", lambda e: settwin.fontColourBlue(window))
    window.bind("<U>", lambda e: settwin.fontColourWhite(window))
    window.bind("+", lambda e: settwin.fontSizeIncrease(window))
    window.bind("-", lambda e: settwin.fontSizeDecrease(window))

    window.mainloop()

if __name__ == '__main__':
    main()
