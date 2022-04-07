import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
#import gui # import the gui file/class

##Creating an array for commands
import re
import array

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
except:
    pass

print(command)
# will call the code to display the date and time
if 'time' in command:
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)
elif 'joke' in command:
    talk(pyjokes.get_joke())
# will call code for setting the text size
elif 'text' and 'size' in command:
    fontSize = re.sub('\D', '', command)
    print(fontSize)
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
elif 'text' and 'colour' | 'text' and 'color' in command:
    #Call method in GUI class responsible for setting the text colour
    pass
# will call code for setting the text position
elif 'text' and 'left' | 'text' and 'right' | 'text' and 'middle' in command:
    #Call method in Visual GUI class to set text GUI position (user speech)
    pass
# will call code responsible for starting the audio listening for converstion
elif 'conversation' and 'started' in command:
    #Call method from Audio class "Google Audio to text"
    #Then, pass output to GUI text area (to display)
    pass
# will call code responsible for stopping the audio listening for converstion
elif 'conversation' and 'ended' in command:
    #Call method to stop displaying text to GUI
    pass
# will call code responsible for turning face detection on/off
elif 'face' and 'detection' in command:
    #Call method to toggle face detection on/off (in visual GUI)
    pass
else:
    talk('Please repeate that command')
