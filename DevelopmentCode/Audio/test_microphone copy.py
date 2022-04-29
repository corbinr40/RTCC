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

try:
    device_info = sd.query_devices(0, 'input')
    samplerate = int(device_info['default_samplerate'])

    model = Model("model")

    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=0, dtype='int16',
                            channels=1, callback=callback):

            rec = KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    print(str(rec.Result()).replace('{', '').replace('}','').replace('text','').replace('"','').replace(':',''))
                else:
                    print(str(rec.PartialResult()).replace('{', '').replace('}','').replace('partial','').replace('"','').replace(':',''))


except KeyboardInterrupt:
    print('\nDone')
except Exception as e:
    pass
