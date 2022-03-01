"""
    This class contains the code responsible for getting audio from the mic and saving it to an audio file.
"""

# import Libraries
import sounddevice as sd  # used to detect/record audio
from scipy.io.wavfile import write  # allows for audio to be "written" to a file
from scipy.io import wavfile 
import numpy as np

# initial values
# frequency of audio
init_fps = 44100
# duration of recording
init_duration = 10

#variable that need to be passed into the class below
durationSet = True 
duration = 10

'''
    [overview]

    [params]
    durationSet: boolean for if the audio duration is set or not
    duration: is the duration of the audio recording if it is set
'''
class CaptureAudio():
    #constuctor
    def __init__(self): 
        super().__init__()

        # calls the function that will capture the audio
        if durationSet == True:
            init_duration = duration
            recorded = self.capture(init_fps, init_duration)
        else:
            recorded = self.capture(init_fps, init_duration)
        
        # save recording as wav file
        int_audio_data = (np.iinfo(np.int32).max*(recorded/np.abs(recorded).max())).astype(np.int32)
        wavfile.write("output.wav",init_fps,int_audio_data)


    # function that will be called for audio capture
    def capture(self, fps, duration):
        print("Recording Started")
        recording = sd.rec(int(duration * fps), samplerate=fps, channels=2)
        sd.wait()
        print("Recording has finished")
        return recording

main = CaptureAudio() # call to class, will need to be called in UI 