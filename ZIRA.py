from tkinter import *
import tkinter.messagebox
import keyboard
import stopwatch
import subprocess
import ZIRAbackend
import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
from playsound import playsound
import misc

#Creates the GUI window screen
mainwindow = Tk(screenName="ZIRA")

#Sets the background colour
mainwindow.configure(background = "#0C4C5D")

#Wishes the user according the time 
misc.wishMe()

#Welcomes the user
engine = tts.init()
engine.say('I am your personal assistant Zira.')
engine.runAndWait()

#Loading the photo
photo = PhotoImage(file = r"C:\Users\anshc\OneDrive\Documents\ZIRA\rsz_apollobutton.png")

#Changing the Title
mainwindow.title("ZIRA")

#Creating Heading text
headinglabel = Label(mainwindow, text="ZIRA - THE VIRTUAL ASSISTANT", bg= '#0C4C5D', fg= "white", font='Bahnschrift 24 bold')

#Creating button
btncreateitems = Button(mainwindow, text='Click here to ask me anything', image = photo ,width=300, font='times 20 bold', command=ZIRAbackend.zira)

#Placing the heading text and button
headinglabel.place(relx=0.5, rely=0.1, anchor=CENTER)
btncreateitems.place(relx=0.5, rely=0.5, anchor=CENTER)

#Specifies the dimensions of the screen 
width = 800
height = 500
screenwidth = mainwindow.winfo_screenwidth()
screenheight = mainwindow.winfo_screenheight()

# Make it center screen
x = str(int(screenwidth / 2 - width / 2))
y = str(int(screenheight / 2 - height / 2))
s = '800x500+' + x + '+' + y
mainwindow.geometry(s)
mainwindow.resizable(width=False, height=False)

#Terminates the GUI
mainwindow.mainloop()
