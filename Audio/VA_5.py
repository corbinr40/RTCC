import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
#import gui # import the gui file/class

##Creating an array for commands
import re
import sys
import array

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#running = True


def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
##                print(command)
                executeCommand(command)
    except:
        pass
    
def executeCommand(command):
    print(command)
    # will call the code to display the date and time
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    # will call code for setting the text size
    elif 'size' in command:
        fontSize = re.sub('\D', '', command)
        print(fontSize)
        talk(fontSize)
    ##    fontSize = array.array('i')
    ##    #fontSize = [command.replace('text', '').replace('size', '')]
    ##    fontSizeInt = command.replace('text', '').replace('size', '')
    ##    fontSize.insert(0, type(int(fontSizeInt)))
    ##    print(fontSize[0])
    ##        command = command.replace('text', '')
    ##        command = command.replace('size', '')
    ##        if int(command)
    ##        gui.set_text_size(int size)
    # will call code for setting the text colour
    elif 'colour' in command:
        print(command)
        #Call method in GUI class responsible for setting the text colour
        colours['red','blue','green','black']
        if command in colours:
            #Check if clours
            print("found")
        else:
            print("not found")
    # will call code for setting the text position
##    elif 'text' and 'left' | 'text' and 'right' | 'text' and 'middle' in command:
##        #Call method in Visual GUI class to set text GUI position (user speech)
##        pass
    # will call code responsible for starting the audio listening for converstion
    elif 'conversation' and 'started' in command:
        #Call method from Audio class "Google Audio to text"
        #Then, pass output to GUI text area (to display)
        pass
    # will call code responsible for stopping the audio listening for converstion
    elif 'ended' in command:
        #Call method to stop displaying text to GUI
        pass
    # will call code responsible for turning face detection on/off
    elif 'face' and 'detection' in command:
        #Call method to toggle face detection on/off (in visual GUI)
        pass
    elif 'power' and 'down' in command:
        talk("Goodbye")
        quit()
        running = False
        sys.exit("Powering Down")
    else:
        print("Not a command")
        talk('Please repeate that command')

if __name__ == '__main__':
    try:
        while True:
            takeCommand()
    except KeyboardInterrupt:
        print("Raising SystemExit")
        raise SystemExit
    #takeCommand()
