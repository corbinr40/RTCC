"""
    This class contains the code responsible for getting audio from the mic and saving it to an audio file.
"""

# import Libraries
import sounddevice as sd  # used to detect/record audio
from scipy.io.wavfile import write  # allows for audio to be "written" to a file


# TODO
# add a if else statement so the recording duration and fps can be altered

# function that will be called for audio capture
def capture(fps, duration):
    print("Recording Started")
    recording = sd.rec(int(duration * fps), samplerate=fps, channels=2)
    sd.wait()
    print("Recording has finished")
    return recording


# initial values
# frequency of audio
init_fps = 44100
# duration of recording
init_duration = 10

# calls the function that will capture the audio
recorded = capture(init_fps, init_duration)

# save recording as wav file
write("output.wav", init_fps, recorded)
