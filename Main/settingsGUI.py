## TKinter test to have a window open in the center of the screen

from tkinter import *
import platform
import configparser

global fontSize
global fontColour
global wakeWord

config = configparser.ConfigParser()
config.read('settings.ini')
fontSize = config['USER SETTINGS']['fontSize']
fontColour = config['USER SETTINGS']['fontColour']
wakeWord = config['USER SETTINGS']['wakeWord']

#fontSize = 0
#fontColour = ''
#wakeWord = ''

#fontSize = 24
#fontColour = 'black'
#wakeWord = 'alexa'




#win.mainloop()


class Settings(Frame):

    def __init__(sett):
        super().__init__()
        #window = Tk()  # Creating instance of Tk class


        window.title("Settings")
        window.resizable(False, False)  # This code helps to disable windows from resizing

        window_height = 700
        window_width = 500

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        window.geometry("{}x{}+{}+{}".format(window_width,
                    window_height, x_cordinate, y_cordinate))

        sett.settingsTitleLabel = Label(text='Settings', font=('', (int(fontSize) * (2))), fg= fontColour)
        sett.settingsTitleLabel.pack(side= TOP, fill= X)

        sett.fontSizeLabel = Label(text='Font Size:', font=('', fontSize), fg=fontColour)
        sett.fontSizeLabel.pack(row=1, column=0)

        sett.currentFontSizeLabel = Label(text=fontSize, font=('', fontSize), fg=fontColour)
        sett.currentFontSizeLabel.pack(row=1, column=1)

        sett.fontColourLabel = Label(text='Font Colour:', font=('', fontSize), fg=fontColour)
        sett.fontColourLabel.pack(row=2, column=0)

        sett.currentFontColourLabel = Label( text=fontColour, font=('', fontSize), fg=fontColour)
        sett.currentFontColourLabel.pack(row=2, column=1)

        sett.wakeWordLabel = Label(text='Wake Word:', font=('', fontSize), fg=fontColour)
        sett.wakeWordLabel.pack(row=3, column=0)

        sett.currentWakeWordLabel = Label( text=wakeWord, font=('', fontSize), fg=fontColour)
        sett.currentWakeWordLabel.pack(row=3, column=1)

        sett.powerLabel = Label(text='Power', font=('', fontSize), fg=fontColour)
        sett.powerLabel.pack(row=4, column=0)

        sett.closeLabel = Label(text='Close', font=('', fontSize), fg=fontColour)
        sett.closeLabel.pack(row=5, column=0)

        #sett.pack()
    
    def fontColourBlue(sett):
        print("Shift I pressed for Blue")
        global fontColour
        fontColour = 'blue'
        sett.currentFontColourLabel.config(text = fontColour)
        sett.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontColourRed(sett):
        print("Shift P pressed for Red")
        global fontColour
        fontColour = 'red'
        sett.currentFontColourLabel.config(text=fontColour)
        sett.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontColourGreen(sett):
        print("Shift O pressed for Green")
        global fontColour
        fontColour = 'green'
        sett.currentFontColourLabel.config(text=fontColour)
        sett.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontColourBlack(sett):
        print("Shift U pressed for Black")
        global fontColour
        fontColour = 'black'
        sett.currentFontColourLabel.config(text=fontColour)
        sett.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontSizeIncrease(sett):
        global fontSize
        if(int(fontSize) <= 38):
            fontSize = int(fontSize) + 2
            sett.refresh()
            config.set('USER SETTINGS', 'fontSize', str(fontSize))
            pass
        pass

    def fontSizeDecrease(sett):
        global fontSize
        if(int(fontSize) >= 10):
            fontSize = int(fontSize) - 2
            sett.refresh()
            config.set('USER SETTINGS', 'fontSize', str(fontSize))
            pass
        pass

    def refresh(sett):
        sett.destroy()
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        sett.__init__()


def closeProgram(e):
    window.destroy()

def settingsStart():
    global window
    global fontSize
    global fontColour
    global wakeWord
    window = Tk()

    settwin = Settings()

    #window.wm_attributes("-topmost", True)
    #window.attributes("-fullscreen", True)

    print(platform.system().lower())

    if('linux' in platform.system().lower()):
        window.wm_attributes('-type', 'splash')
    else:
        pass

    window.bind("<Escape>", lambda e: closeProgram(e))
    window.bind("<P>", lambda e: settwin.fontColourRed())
    window.bind("<O>", lambda e: settwin.fontColourGreen())
    window.bind("<I>", lambda e: settwin.fontColourBlue())
    window.bind("<U>", lambda e: settwin.fontColourBlack())
    window.bind("+", lambda e: settwin.fontSizeIncrease())
    window.bind("-", lambda e: settwin.fontSizeDecrease())
    window.mainloop()


if __name__ == '__main__':
    settingsStart()
