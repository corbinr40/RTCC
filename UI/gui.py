#import the libraries required
from cgitb import text
from email.policy import default
from multiprocessing.sharedctypes import Value
#from this import d
from tkinter import * 
from tkinter import font
from tkinter import colorchooser

#set up the UI window
root = Tk()
root.title('Basic form of UI')
root.geometry("500x450")

#method for openening the text file of the saved audio
def open_text():
  #will potentially use a+ to append new speach to the text file istead of just r for read
  text_file = open("C:\\Users\\Jordan\\RTCC\\output.txt",'r') 
  text_output.insert(END,text_file.read())
  text_file.close()

#method for starting the audio capture 
def start_rec():
  #TODO
  pass
#method for stopping the audio capture
def stop_rec():
  #TODO
  pass

#method for making the text bold
def text_bold():
  #create font
  bold_font = font.Font(text_output, text_output.cget("font"))
  bold_font.configure(weight="bold")
  #configure the tag
  text_output.tag_configure("bold", font=bold_font)
  #define current_tags
  current_tags = text_output.tag_names("sel.first")
  #If to see if tag is set
  if "bold" in current_tags:
    text_output.tag_remove("bold","sel.first","sel.last")
  else:
    text_output.tag_add("bold","sel.first","sel.last")
    
#method for making the text Italic
def text_italic():
  #create font
  italic_font = font.Font(text_output, text_output.cget("font"))
  italic_font.configure(slant="italic")
  #configure the tag
  text_output.tag_configure("italic", font=italic_font)
  #define current_tags
  current_tags = text_output.tag_names("sel.first")
  #If to see if tag is set
  if "italic" in current_tags:
    text_output.tag_remove("italic","sel.first","sel.last")
  else:
    text_output.tag_add("italic","sel.first","sel.last")
    
#Change text colour for selected words 
def text_colour():
  #pick a colour
  text_colour = colorchooser.askcolor()[1] 
  if text_colour:
    #create font
    colour_font = font.Font(text_output, text_output.cget("font"))
    #configure the tag
    text_output.tag_configure("coloured", font=colour_font,foreground=text_colour)
    #define current_tags
    current_tags = text_output.tag_names("sel.first")
    #If to see if tag is set
    if "colured" in current_tags:
      text_output.tag_remove("coloured","sel.first","sel.last")
    else:
      text_output.tag_add("coloured","sel.first","sel.last")

#change all text colour
def all_text_colour():
  #pick a colour
  text_colour = colorchooser.askcolor()[1] 
  if text_colour:
    print(text_colour)
    text_output.config(fg=text_colour)

#change the background colour
def bg_colour():
  #pick a colour
  text_colour = colorchooser.askcolor()[1] 
  if text_colour:
    text_output.config(bg=text_colour)
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#Create Main Frame
main_frame = Frame(root)
main_frame.pack(pady=5)

#create scrollbar for text output
text_scroll = Scrollbar(main_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#create the text area   
text_output  = Text(main_frame, width=40,height=10, font=("Helvetica",16),yscrollcommand=text_scroll.set)
text_output.pack(pady = 20)

#configure the scrollbar
text_scroll.config(command=text_output.yview)

#Create settings menu
settings_menu = Menu(root)
root.config(menu=settings_menu)

#Add options menu
options_menu = Menu(settings_menu,tearoff=False)
settings_menu.add_cascade(label="Settings", menu=options_menu)
options_menu.add_command(label= "Font Size")

#Add Font colour options to menu
colour_menu = Menu(options_menu,tearoff=False)
options_menu.add_cascade(label="Colour", menu=colour_menu)
colour_menu.add_command(label= "Selected Text",command=text_colour)
colour_menu.add_command(label= "All Text",command=all_text_colour)
colour_menu.add_command(label= "Background",command=bg_colour)

#Add Font style options to menu
fontstyle_menu = Menu(options_menu,tearoff=False)
options_menu.add_cascade(label="Font Style", menu=fontstyle_menu)
fontstyle_menu.add_command(label= "Bold",command=text_bold)
fontstyle_menu.add_command(label= "Italic",command=text_italic)

options_menu.add_command(label= "Text Location")
options_menu.add_command(label= "Face Detection")
options_menu.add_separator()
options_menu.add_command(label= "Advanced Settings")

#Add status bar to Bottom of UI
status_bar = Label(root, text='Ready  ',anchor=E)
status_bar.pack(fill = X, side=BOTTOM,ipady=5)

#create button to open the file 
open_button = Button(root, text="Open Text File", command=open_text)
open_button.pack(pady = 20)

#creates button to start record the audio
start_button = Button(root, text="Start Recording", command=start_rec)
start_button.pack(pady = 20)

#creates button to stop recording audio
stop_button = Button(root, text="Stop Recording", command=stop_rec)
stop_button.pack(pady = 20)

root.mainloop()