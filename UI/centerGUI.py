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

    def __init__(self):
        super().__init__()
        #root = Tk()  # Creating instance of Tk class


        root.title("Settings")
        root.resizable(False, False)  # This code helps to disable windows from resizing

        window_height = 700
        window_width = 500

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        root.geometry("{}x{}+{}+{}".format(window_width,
                    window_height, x_cordinate, y_cordinate))

        self.settingsTitleLabel = Label(text='Settings', font=('', (int(fontSize) * (2))), fg= fontColour)
        self.settingsTitleLabel.grid(row=0, column=1, columnspan=2)

        self.fontSizeLabel = Label(text='Font Size:', font=('', fontSize), fg=fontColour)
        self.fontSizeLabel.grid(row=1, column=0)

        self.currentFontSizeLabel = Label(text=fontSize, font=('', fontSize), fg=fontColour)
        self.currentFontSizeLabel.grid(row=1, column=1)

        self.fontColourLabel = Label(text='Font Colour:', font=('', fontSize), fg=fontColour)
        self.fontColourLabel.grid(row=2, column=0)

        self.currentFontColourLabel = Label( text=fontColour, font=('', fontSize), fg=fontColour)
        self.currentFontColourLabel.grid(row=2, column=1)

        self.wakeWordLabel = Label(text='Wake Word:', font=('', fontSize), fg=fontColour)
        self.wakeWordLabel.grid(row=3, column=0)

        self.currentWakeWordLabel = Label( text=wakeWord, font=('', fontSize), fg=fontColour)
        self.currentWakeWordLabel.grid(row=3, column=1)

        self.powerLabel = Label(text='Power', font=('', fontSize), fg=fontColour)
        self.powerLabel.grid(row=4, column=0)

        self.closeLabel = Label(text='Close', font=('', fontSize), fg=fontColour)
        self.closeLabel.grid(row=5, column=0)

        #self.pack()
    
    def fontColourBlue(self):
        print("Shift I pressed for Blue")
        global fontColour
        fontColour = 'blue'
        self.currentFontColourLabel.config(text = fontColour)
        self.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontColourRed(self):
        print("Shift P pressed for Red")
        global fontColour
        fontColour = 'red'
        self.currentFontColourLabel.config(text=fontColour)
        self.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontColourGreen(self):
        print("Shift O pressed for Green")
        global fontColour
        fontColour = 'green'
        self.currentFontColourLabel.config(text=fontColour)
        self.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontColourBlack(self):
        print("Shift U pressed for Black")
        global fontColour
        fontColour = 'black'
        self.currentFontColourLabel.config(text=fontColour)
        self.refresh()
        config.set('USER SETTINGS', 'fontColour', str(fontColour))
        pass

    def fontSizeIncrease(self):
        global fontSize
        if(int(fontSize) <= 38):
            fontSize = int(fontSize) + 2
            self.refresh()
            config.set('USER SETTINGS', 'fontSize', str(fontSize))
            pass
        pass

    def fontSizeDecrease(self):
        global fontSize
        if(int(fontSize) >= 10):
            fontSize = int(fontSize) - 2
            self.refresh()
            config.set('USER SETTINGS', 'fontSize', str(fontSize))
            pass
        pass

    def refresh(self):
        self.destroy()
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        self.__init__()


def closeProgram(e):
    root.destroy()

def settingsStart():
    global root
    global fontSize
    global fontColour
    global wakeWord
    root = Tk()

    ex = Settings()

    #root.wm_attributes("-topmost", True)
    #root.attributes("-fullscreen", True)

    print(platform.system().lower())

    if('linux' in platform.system().lower()):
        root.wm_attributes('-type', 'splash')
    else:
        pass

    root.bind("<Escape>", lambda e: closeProgram(e))
    root.bind("<P>", lambda e: ex.fontColourRed())
    root.bind("<O>", lambda e: ex.fontColourGreen())
    root.bind("<I>", lambda e: ex.fontColourBlue())
    root.bind("<U>", lambda e: ex.fontColourBlack())
    root.bind("+", lambda e: ex.fontSizeIncrease())
    root.bind("-", lambda e: ex.fontSizeDecrease())
    root.mainloop()


if __name__ == '__main__':
    settingsStart()
