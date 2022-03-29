''' 
  This is a virtual assistant program that will listen for a wake word and once triggered it will process some commands to 
  alter settings, begin capturing audio and stop capturing audio
'''
#import the libraries needed
import pyttsx3 as p 
import speech_recognition as sr
import pywhatkit 
import datetime
import wikipedia
import pyjokes 

#create listener
r = sr.Recognizer()
#initialise the engine
engine = p.init()
#set the speed of the audio
rate = engine.getProperty('rate')
engine.setProperty('rate',200)
#set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#function for getting the virtual assistant to speak
def speak(text):
  engine.say(text)
  #asks computer to wait till sentance is finished
  engine.runAndWait() 

#function called when a command prompts the Virtual Assistant to begin listening
def take_Command():
  try:
    with sr.Microphone() as source:
      #set spectrum range of voice capture
      r.energy_threshold = 10000
      #remove background noise
      r.adjust_for_abient_noise(source,1.2)
      print("listening ... ")
      #capture the audio 
      audio = r.listen(source)
      #send it to the google engine for speech to text
      command = r.recognize_google(audio)
      command = command.lower()
      #if the key word is in the command 
      if 'alexa' in command:
        command = command.replace('alexa','') ##########################replace with our key word
        print(command)
  except:
    pass
  return command 

#function called to take command from the user
def run_assistant():
  command = take_Command()
  ############################################ REMOVE (just here for testing)
  print(command)
  if 'play' in command:
    song = command.replace('play', '')
    speak("now playing " + song)
    pywhatkit.playonyt(song)
  elif 'time' in command:
    time = datetime.datetime.now().strftime('%H:%M')
    speak('the time currently is' + time)
  elif 'wikipedia' in command:
    Question = command.replace('wikipedia','')
    info = wikipedia.summary(Question,1)
    speak(info)
  elif 'joke' in command:  
    speak(pyjokes.get_joke())
  ######################################################################################
  #will call code for setting the text size
  elif 'text' and 'size' in command:  
    pass
  #will call code for setting the text colour
  elif 'text' and 'colour' | 'text' and 'color' in command:  
    pass
  #will call code for setting the text position
  elif 'text' and 'left' | 'text' and 'right' | 'text' and 'middle' in command:  
    pass
  #will call code responsible for starting the audio listening for converstion 
  elif 'conversation' and 'started' in command:  
    pass
  #will call code responsible for stopping the audio listening for converstion 
  elif 'conversation' and 'ended' in command:  
    pass
  #will call code responsible for turning face detection on/off
  elif 'face' and 'detection' in command:  
    pass
  else:
    speak('Please repeate that command')  
    
while True:
  run_assistant()

  
  
  
  
  
  
  
  
  