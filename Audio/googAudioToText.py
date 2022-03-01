import speech_recognition as sr
from os import path
from pydub import AudioSegment

#creates object of speach recogniser
r = sr.Recognizer()
#read audio file into an audio variable
with sr.AudioFile('C:\\Users\\Jorda\\OneDrive\\Desktop\\RTCC-main\\output.wav') as source: 
        audio = r.listen(source)
        try:
                #can change google to other later
                #pass it the audio data
                text= r.recognize_google(audio)
                print("working on...")
                #saves text output to a txt file
                with open('output.txt', 'w') as f:
                        f.write(text)
        except:
                print("sorry, didn't work")


