<div id="top"></div>

<!-- PROJECT SHIELDS -->

<!-- [![Contributors][contributors-shield]][contributors-url] -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/corbinr40/RTCC">
    <img src="images/logo.png" alt="Logo" width="320" height="200">
  </a>

<h3 align="center">RTCC</h3>

  <p align="center">
    RTCC, or <i>Real Time Communication Captions</i>, is a piece of software that converts voice to text in a visual output, as an aid to individuals who are hard of hearing. The plan is to deliver this via a piece of hardware in the form of glasses with a heads up display. However a fallback of this would be an app that fulfils this. The system will work by using facial detection to track who is talking to place the converted audio appropriately.
    <br />
    <a href="https://github.com/corbinr40/RTCC"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/corbinr40/RTCC">View Demo</a>
    ·
    <a href="https://github.com/corbinr40/RTCC/issues">Report Bug</a>
    ·
    <a href="https://github.com/corbinr40/RTCC/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

RTCC is broken down into 4 main areas: audio, visual, UI, and hardware. The audio component focuses on taking audio in from the user, processing it and then outputting, along with handeling audio commands for system processes. The visual component will use a camera to look for a face, detect where it is and pass the data onto the UI. The UI handles all of the aspects which the user sees and interacts with. Finally, the hardware component is making sure all of the software works efficiently and cohesive with one another.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.10](https://www.python.org/)
* [OpenCV](https://opencv.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
There are a few dependencies for running this software. The software has been created for the *Raspberry Pi Zero W 2* but can also run on *Windows* and *Mac*.
### Hardware (tested)
- [Raspberry Pi Zero W 2]()
- [Adafruit I2S Microphone]()
- [Raspberry Pi Camera]()
- [Battery Pack Device]()

### Software

#### Operating System (tested)
- [Raspian OS]()
- [MacOSX]()
- [Windows 10]()
#### Required Modules
##### All
- [faulthandler]()
- [pstats]()
- [tkinter]()
- [datetime]()
- [time]()
- [platform]()
- [multiprocessing]()
- [numpy]()
- [OpenCV - Python](https://pypi.org/project/opencv-python/)
- [threading]()
- [speech recognition]()
- [pyjokes]()
- [re]()
- [configparser]()
##### Raspian Specific
- [smbus]()

### Prerequisites

#### All
These all require `pip` to be installed
```shell
    pip3 install numpy
    pip3 install opencv-python
    pip3 install pyjokes
```

#### Raspian (specific)
To get SpeechRecognition installed, PyAudio is required and installed though apt-get.
```sh
PyAudio:

  sudo apt-get install python-dev
  sudo apt-get install portaudio19-dev
  sudo pip install pyaudio

Speech Recognition:

  pip3 install SpeechRecognition
```

#### MacOS (specific)
To get SpeechRecognition installed, PyAudio (pip) is required and PortAudio ([Homebrew]()).
```sh
PortAudio:

  brew install portaudio

PyAudio:

  pip3 install pyaudio

Speech Recognition:

  pip3 install SpeechRecognition
```

#### Windows (specific)
To get SpeechRecognition installed, [PipWin]() is required to install pyaudio.
```powershell
PipWin:

  pip install pipwin

PyAudio:

  pipwin install pyaudio

Speech Recognition:

  pip install SpeechRecognition
```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/corbinr40/rtcc.git
   ```
2. Make sure all required modules are installed
3. Run the `checker.py` file
   ```sh
   python3 checker.py
   ```
4. Once all the modules have been installed, the program can be ran
    ```sh
    cd Main/

    python3 main.py
    ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The program is intended for use with voice commands, but does have them bound to keys for debugging/use without microphone

### Voice commands
All voice commands require the **wake word** to activate.

As default, the wake word is "***glass***"

All commands follow the format of:
```
    <wake word> <command>
```

Example:
```
    glass activate face detection
```
#### List of commands
* **face detection** - Activate/Deactivate face detection
* **voice detection** - Activate/Deactivate voice detection
* **settings** - Show settings
* **commands** - Show command list
* **shut down** - Close program
* **set font colour red** - Set font colour to Red
* **set font colour green** - Set font colour to Green
* **set font colour blue** - Set font colour to Blue
* **set font colour white** - Set font colour to White
* **increase font size** - Increase font size
* **decrease font size** - Decrease font size

### Key combines
**All are case-sensitive**
#### System Wide
* <kbd>o</kbd> - Activate/Deactivate face detection
* <kbd>p</kbd> - Activate/Deactivate voice detection
* <kbd>s</kbd> - Show settings
* <kbd>c</kbd> - Show command list
* <kbd>escape</kbd> - Close program

#### Settings only
* <kbd>P</kbd> - Set font colour to Red
* <kbd>O</kbd> - Set font colour to Green
* <kbd>I</kbd> - Set font colour to Blue
* <kbd>U</kbd> - Set font colour to White
* <kbd>+</kbd> - Increase font size
* <kbd>-</kbd> - Decrease font size

<p align="right">(<a href="#top">back to top</a>)</p>

## Program Breakdown
### Face Detection and Training Model
Using OpenCV and the Nvidia image library, a face detection model was created. 
The first model was a quick test one to see how well the model works. There were quite a few false positives but overall, it worked. 

![Inacurate Face Detection model][inaccurateFace-screenshot]

```sh
    \opencv\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 7000 -precalcIndBufSize 7000 -numPos 700 -numNeg 1000 -numStages 5 -w 24 -h 24 -maxFalseAlarmRate 0.3 -minHitRate 0.99
```

The next stage was to add more test and training data to make the model more accurate. (Add the code used to create along with the techniques from folder structure)

![Face Detection model working without masks][faceNoMask-screenshot]

![Face Detection model not working with masks][faceNoMaskFail-screenshot]

```sh
    \opencv\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 7000 -precalcIndBufSize 7000 -numPos 2700 -numNeg 5000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.3 -minHitRate 0.99
```

We ran into an issue where people with masks couldn’t be recognised, so we used (mask image library) to bulk up our model. 
Using some test code (show code) we can see how well the model worked. 

![Finalised Face Detection Model][finalFace-screenshot]

```sh
    \opencv\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 7000 -precalcIndBufSize 7000 -numPos 1800 -numNeg 5800 -numStages 16 -w 24 -h 24 -maxFalseAlarmRate 0.3 -minHitRate 0.99
```

### Audio Component
Initially we wanted to record the users speech and save it to a .wav file, then convert this to text. The initial tests of this worked. (Show code and screenshots)

```python
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile 
import numpy as np

init_fps = 44100
init_duration = 10

durationSet = True 
duration = 10

class CaptureAudio():
    def __init__(self): 
        super().__init__()

        if durationSet == True:
            init_duration = duration
            recorded = self.capture(init_fps, init_duration)
        else:
            recorded = self.capture(init_fps, init_duration)
        
        int_audio_data = (np.iinfo(np.int32).max*(recorded/np.abs(recorded).max())).astype(np.int32)
        wavfile.write("output.wav",init_fps,int_audio_data)

    def capture(self, fps, duration):
        print("Recording Started")
        recording = sd.rec(int(duration * fps), samplerate=fps, channels=2)
        sd.wait()
        print("Recording has finished")
        return recording

main = CaptureAudio()
```

```python
import speech_recognition as sr
from os import path
from pydub import AudioSegment

r = sr.Recognizer()
with sr.AudioFile('output.wav') as source: 
        audio = r.listen(source)
        try:
                text= r.recognize_google(audio)
                print("working on...")
                with open('output.txt', 'w') as f:
                        f.write(text)
        except:
                print("sorry, didn't work")
```

![TESTS OF SPEECH DETECTION][testSpeech-screenshot]

Unfortunately we realised it was quite slow so we had to think of away around it. Luckily we wanted to have a way for the user to navigate the system just using their voice, so we needed an AI assistant of sorts. Our thought was “could we use that same technique to get the users voice” and, turns out we could.

```python
def detectVoice(self):
    global audioCheck
    global command
    while True:
        try:
            with sr.Microphone() as source:
                listener.energy_threshold = 10000
                listener.adjust_for_ambient_noise(source, 1.2)
                if(audioCheck == False):
                    global canvas
                    global audioOn
                    self.canvas.itemconfig(audioOn, fill='#000000')
                    pass
                else:
                    self.canvas.itemconfig(audioOn, fill='#F85E2B')
                    print('listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    print(command)
                    if('glass' in command):
                        command = command.replace('glass', '')
                        self.executeCommand(command)
        except Exception as e:
            print(e)
            pass
```

![Finalised SPEECH DETECTION][finalSpeech-screenshot]

### GUI Interface
Compared different GUI libraries (TKinter and PYQT5) ultimately settled on TKinter 
```python
## PyQt5 GUI
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys

x = 490
y = 426
w = 163
h = 163

class MyFirstGUI(QMainWindow): 

    def __init__(self):
        super(MyFirstGUI, self).__init__()
        self.setWindowTitle("Face Location")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        painter.drawRect(x, y, w, h)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MyFirstGUI()
    gui.show()
    sys.exit(app.exec_())
```
```python
## Tkinter GUI
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
        rectFace = canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)
        
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
    
    x1 = 490
    y1 = 426
    x2 = 635
    y2 = 571
    
    global root
    root = Tk()
    ex = Example()
    root.wm_attributes("-topmost", True)
    root.attributes("-fullscreen", True)
    
    root.bind("<Key>", keypress)
    root.bind("<Escape>", lambda e: closeProgram(e))
    root.mainloop()

if __name__ == '__main__':
    main()
```

![PyQt5 vs Tkinter][PyQt5vsTkinterGUI-screenshot]

Implemented face detection to GUI 
```python
def createRect(self,x1, y1, x2, y2):
  global rectFace
  global canvas
  global voiceText
  global fontColour
  global command
  self.canvas.delete(rectFace)
  self.canvas.delete(voiceText)
  rectFace = self.canvas.create_rectangle(x1, y1, x2, y2, outline="#f11", width=2)
  voiceText = self.canvas.create_text((x2 + x1) / 2, (y2 + 25), fill=fontColour, font=('', fontSize), text=command)

def findFace(self):
  try:
    face_cascade = cv2.CascadeClassifier('cascade.xml')

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
      _, img = cap.read()
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.1, 4)
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
    k = cv2.waitKey(30) & 0xff
    if(k == 27):
      cv2.destroyAllWindows()
      break
    except Exception as e:
      cap.release()
      print(e)

def values(self, x1, y1, x2, y2):
  self.createRect(x1, y1, x2, y2)
  return (x1, y1, x2, y2)
```

![Face Detection implemented][faceDetectionOnGUI-screenshot]

Added menu bar to show power and time 
```python
...

  self.currentTimeLabel = Label(menubarFrame)
  self.currentTimeLabel.pack(anchor=N, side=RIGHT)
  self.currentTime()

  self.currentBatteryLabel = Label(menubarFrame)
  self.currentBatteryLabel.pack(anchor=E, side=RIGHT)
  self.currentPower()

...

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

    powerLevel = "{:3.0f}%".format(p)
    self.currentBatteryLabel.config(text= powerLevel)
    self.currentBatteryLabel.after(1000, self.currentPower)
  else:
    self.currentBatteryLabel.config(text="N/A")
```

![Power and Time on menu bar][powerTimeMenu-screenshot]

Added UI feedback for the user to show that the camera and mic is active 
```python
...

  audioOn = self.canvas.create_oval(620, 460, 640, 480, fill="#000000", width=2)
  videoOn = self.canvas.create_oval(590, 460, 610, 480, fill="#000000", width=2)

...

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

```

![UI Feedback][UIFeedback-screenshot]

Implemented ability to change UI elements through key combines (like increase text and change text colour) 
```python
...
root.bind("o", lambda e: pauseFaceDect())
root.bind("p", lambda e: pauseAudioDect())
root.bind("s", lambda e: settingsStart())
root.bind("c", lambda e:  ex.commandsList())
root.bind("<Escape>", lambda e: closeProgram())
...
window.bind("<P>", lambda e: settwin.fontColourRed(window))
window.bind("<O>", lambda e: settwin.fontColourGreen(window))
window.bind("<I>", lambda e: settwin.fontColourBlue(window))
window.bind("<U>", lambda e: settwin.fontColourWhite(window))
window.bind("+", lambda e: settwin.fontSizeIncrease(window))
window.bind("-", lambda e: settwin.fontSizeDecrease(window))
...
```

<!-- ![UI Changes Through Keys][UIKeyChanges-screenshot] -->

A list of commands will be show to the user upon request
```python
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
```

![UI Changes Through Keys][commandList-screenshot]

Implemented voice detection element to gui 
```python
def detectVoice(self):
global audioCheck
global command
while True:
    try:
        with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            if(audioCheck == False):
                global canvas
                global audioOn
                self.canvas.itemconfig(audioOn, fill='#000000')
                pass
            else:
                self.canvas.itemconfig(audioOn, fill='#F85E2B')
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)
                if('glass' in command):
                    command = command.replace('glass', '')
                    self.executeCommand(command)
    except Exception as e:
        print(e)
        pass
```

![Voice In Gui][voiceGUI-screenshot]

Bound voice commands to UI changes 
```python
def executeCommand(self, command):
print(command)
if('joke' in command):
    self.notificationShow(pyjokes.get_joke())
elif('setting' in command):
    settingsThread = threading.Thread(
        target=settingsStart(), args=())
    settingsThread.daemon = True
    settingsThread.start()
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
elif('ended' in command):
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
```

  ![Voice Commands][voiceCommands-screenshot]

Added UI feedback for the user when command is executed/not understood 
  ![Command Notification][commandNotification-screenshot]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Speech Detection
    - [ ] Custom Offline Speech Detection Model
    - [ ] Voice Translation
    - [ ] Develop Speech Detection to be more real time
<!-- - [ ] Face Detection
     - [ ] Nested Feature -->

See the [open issues](https://github.com/corbinr40/rtcc/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Corbin Richardson - [@corbinr40](https://twitter.com/corbinr40)

Jordan Drummond Edwards <!-- - [@TWITTER](https://twitter.com/) -->

Aryaman Anand - [@AryamanAnand](https://twitter.com/AryamanAnand)

Manan Singh <!-- - [@TWITTER](https://twitter.com/) -->

Project Link: [https://github.com/corbinr40/rtcc](https://github.com/corbinr40/rtcc)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p> -->


[forks-shield]: https://img.shields.io/github/forks/corbinr40/rtcc.svg?style=for-the-badge
[forks-url]: https://github.com/corbinr40/rtcc/network/members
[stars-shield]: https://img.shields.io/github/stars/corbinr40/rtcc.svg?style=for-the-badge
[stars-url]: https://github.com/corbinr40/rtcc/stargazers
[issues-shield]: https://img.shields.io/github/issues/corbinr40/rtcc.svg?style=for-the-badge
[issues-url]: https://github.com/corbinr40/rtcc/issues
[license-shield]: https://img.shields.io/github/license/corbinr40/rtcc.svg?style=for-the-badge
[license-url]: https://github.com/corbinr40/rtcc/blob/main/LICENSE.txt
[inaccurateFace-screenshot]: images/inaccurateFace.png
[faceNoMaskFail-screenshot]: images/faceNoMaskFail.png
[faceNoMask-screenshot]: images/faceNoMask.png
[finalFace-screenshot]: images/finalFace.png
[testSpeech-screenshot]: images/testSpeech.png
[finalSpeech-screenshot]: images/finalSpeech.png
[PyQt5vsTkinterGUI-screenshot]: images/PyQt5vsTkinterGUI.png
[faceDetectionOnGUI-screenshot]: images/faceDetectionOnGUI.png
[powerTimeMenu-screenshot]: images/powerTimeMenu.png
[UIFeedback-screenshot]: images/UIFeedback.png
[UIKeyChanges-screenshot]: images/UIKeyChanges.png
[voiceGUI-screenshot]: images/voiceGUI.png
[voiceCommands-screenshot]: images/voiceCommands.png
[commandNotification-screenshot]: images/commandNotification.png
[commandList-screenshot]: images/commandList.png