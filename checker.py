import faulthandler
from numpy import column_stack, size
import configparser
import re
import pyjokes
import speech_recognition as sr
import threading
import cv2
import numpy.core.multiarray
from multiprocessing import Process, Queue, Pipe
import platform
import time
import datetime
from tkinter import *
import pstats

import sys
import subprocess
import pkg_resources

required = {'mutagen', 'gTTS'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


if('linux' in platform.system().lower()):
    try:
        import smbus
        import faulthandler
        from numpy import column_stack, size
        import configparser
        import re
        import pyjokes
        import speech_recognition as sr
        import threading
        import cv2
        import numpy.core.multiarray
        from multiprocessing import Process, Queue, Pipe
        import platform
        import time
        import datetime
        from tkinter import *
        import pstats
    except Exception as e:
        print(e)
else:
    try:
        import faulthandler
        from numpy import column_stack, size
        import configparser
        import re
        import pyjokes
        import speech_recognition as sr
        import threading
        import cv2
        import numpy.core.multiarray
        from multiprocessing import Process, Queue, Pipe
        import platform
        import time
        import datetime
        from tkinter import *
        import pstats
    except Exception as e:
        print(e)

import Main.main as facedetection

facedetection.main()
