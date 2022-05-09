import platform

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

        print("All required modules are installed!\nrun: python3 Main/main.py")
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
        
        print("All required modules are installed!\nrun: python3 Main/main.py")
    except Exception as e:
        print(e)
