import speech_recognition as sr
#import pyttsx3
import datetime
import pyjokes
#import gui # import the gui file/class

##Creating an array for commands
import re
#import sys
#import array


#from FaceGUI.py import main
#import FaceGUI as face

listener = sr.Recognizer()
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

#running = True


#def talk(text):
#    engine.say(text)
#    engine.runAndWait()

def detectVoice():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #command = listener.recognize_sphinx(voice)
            command = command.lower()
            print(command)
            if 'alexa' in command:
                command = command.replace('alexa', '')
##                print(command)
                executeCommand(command)
    except Exception as e:
        print(e)
        pass
    
def executeCommand(command):
    print(command)
    # will call the code to display the date and time
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
    elif 'joke' in command:
        print(pyjokes.get_joke())
    # will call code for setting the text size
    elif 'size' in command:
        fontSize = re.sub('\D', '', command)
        print(fontSize)
        print(fontSize)
    elif 'colour' in command:
        print(command)
        #Call method in GUI class responsible for setting the text colour
        colours = ['red','blue','green','black']
        if any(r in command for r in colours):
            print("Found")
        else:
            print("Not Found")

    # will call code for setting the text position
##    elif 'text' and 'left' | 'text' and 'right' | 'text' and 'middle' in command:
##        #Call method in Visual GUI class to set text GUI position (user speech)
##        pass
    # will call code responsible for starting the audio listening for converstion
    elif 'conversation' and 'started' in command:
        output = command.replace('conversation','').replace('started','')
        DisplayText(output,True)
# will call code responsible for stopping the audio listening for converstion
    elif 'ended' in command:
        output = "conversation finished"
        DisplayText(output, False)
    elif 'face' and 'detection' in command:
        #Call method to toggle face detection on/off (in visual GUI)
##        if 'off' in command:
##            faceDetect = False
##        else:
##            faceDetect = True
##        faceToggle(faceDetect
        #face.main()
        pass
    elif 'power' and 'down' in command:
        print("Goodbye")
        quit()
    else:
        print("Not a command")
        print('Please repeate that command')

if __name__ == '__main__':
    try:
        while True:
            detectVoice()
    except KeyboardInterrupt:
        print("Raising SystemExit")
        raise SystemExit
    #detectVoice()
