import speech_recognition as sr
import pyttsx3 as p

r = sr.Recognizer()
engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source)
        command = r.recognize_google(audio)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
except:
    pass
