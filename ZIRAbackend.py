import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
from playsound import playsound
from os import popen
import yagmail
from sys import exit
import keyboard
import stopwatch
import subprocess
import wikipedia
import misc
import IPpractice

# defining a function zira()
def zira():
            #initialise the text-to-speech
            engine = tts.init()
            # content for text-to-speech 
            engine.say('Yes sir')
            #terminate the text-to-speech
            engine.runAndWait()
            # initialize the audio inout using the microphone and saving it in a variable 'r'
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak anything you want me to do:")
                # play the double-beep sound
                playsound('C:\double-beep.mp3')
                # saving the audio in a variale "r"
                audio = r.listen(source)
                try:
                    # analyzes the speech input and converts it into text using Google Voice Recognition
                    text = r.recognize_google(audio)
                    # to print what the computer recognized from your speech
                    print("You said : {}".format(text))
                except:
                    print("Sorry could not recognize what you said")
                    text = "what can you do"
                task = text
            
            # gives weather updates using the weather module
            if task == "weather report":
                engine = tts.init()
                engine.say('Thunderstorms will move through your area. The high will be 28 and low will be 23.')
                engine.runAndWait()
            

            elif task == "what is 0 + 0":
                engine = tts.init()
                engine.say("Zero plus Zero is nothing. Zero")
                engine.runAndWait()
            
            elif task == "what can you do":
                engine = tts.init()
                engine.say("I can perform various functions like sending e-mails, downloading songs and cracking a joke!")
                engine.runAndWait()

            # for cracking a fun joke
            elif task == "knock knock":
                engine = tts.init()
                engine.say("Who's there?")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print("You said: "+ text)
                    except:
                        text = "Baahubali"
                
                if text == "You cant see me":
                    engine = tts.init()
                    engine.say("That is John Cena")
                    engine.runAndWait()

                else:
                    engine = tts.init()
                    engine.say("Try again")
                    engine.runAndWait()

            # tells you a joke
            elif task == "tell me a joke" or "joke" in task:
                engine = tts.init()
                engine.say("What did the green peas say? Nothing. They just mutter'ed.")
                engine.runAndWait()

            # gives menu ideas
            elif task == "give me menu ideas" or "menu ideas" in task:
                engine = tts.init()
                engine.say("Toss some bhel and sprouts together for breakfast, keep it simple with a sandwich for lunch and have vegetable fajitas with soy rice for dinner.")
                engine.runAndWait()

            elif task == "give me a gross fact" or "gross fact" in task:
                engine = tts.init()
                engine.say("Breaking news! Farts can travel at speeds of up to 10 feet per second.")
                engine.runAndWait()
            
            # uses the stopwatch module to run a stopwatch in the app 
            elif task == "start stopwatch" or "stopwatch" in task:
                engine = tts.init()
                engine.say("press Enter to start")
                engine.runAndWait()
                stopwatch() # refer the stopwatch module for reference
            
            elif task == "Hindi tongue twister":
                engine = tts.init()
                engine.say("Kaccha paapad, pakka paapad, kaccha paapad, pakka paapad, kaccha paapad, pakka paapad.")
                engine.runAndWait()

            elif task == "am I fat":
                engine = tts.init()
                engine.say("I would prefer not to say")
                engine.runAndWait()

            elif task == "what are you wearing" or "you wearing" in task:
                engine = tts.init()
                engine.say("Aluminosilcate glass and Alcantara. Nice,huh?")
                engine.runAndWait()

            # sends a mail using the yagmail module 
            elif task == "send a mail":
                engine = tts.init()
                engine.say("Fill out the following details to send the mail.")
                engine.runAndWait()
                # the moldule IPpractice is used to 
                IPpractice.sendmail()
                engine = tts.init()
                engine.say("Mail sent.")
                engine.runAndWait()

            elif task == "what is the best laptop" or "best laptop" in task:
                engine = tts.init()
                engine.say("The one you're using.")
                engine.runAndWait()

            elif task == "will you marry me" or "marry me" in task:
                engine = tts.init()
                engine.say("Lets just be friends. OK?")
                engine.runAndWait()

            # opens spotify using the popen module
            elif task == "open spotify" or "spotify" in task:
                engine = tts.init()
                engine.say("Opening Spotify")
                engine.runAndWait()
                popen('spotify')

            elif task == "tell me a story" or "story" in task:
                engine = tts.init()
                engine.say("Once upon a time.... No, it's too silly.")
                engine.runAndWait()

            elif task == "how are you":
                engine = tts.init()
                engine.say("I am in good health! Thank you for asking!")
                engine.runAndWait()
            
            elif task == "how old are you":
                engine = tts.init()
                engine.say("I was created on 15th August 2018 by Ansh Choudhary. Feels like only yesterday.")
                engine.runAndWait()
            
            # takes text inputs to display the Google results 
            elif task == "search on Google":
                engine = tts.init()
                engine.say("Please type what you want to search on Google: ")
                engine.runAndWait()
                searchTerm = input("Search on google: ")
                wb.open("https://www.google.com/?#q="+searchTerm) #webbrowser is used to browse the internet

            elif task == "f*** you":
                engine = tts.init()
                engine.say("Haters gonna hate")
                engine.runAndWait()

            # locates the place on Google Maps as per the text input
            elif task == "locate a place":
                address = input("Enter the address: ")
                engine = tts.init()
                engine.say("Locating {}".format(address))
                engine.runAndWait()
                wb.open('https://www.google.com/maps/place/' + address)  #webbrowser is used to browse the internet
                
            elif task == "what is the meaning of life" or "meaning of life" in task:
                engine = tts.init()
                engine.say("All evidence to date suggests it's chocolate")
                engine.runAndWait()

            elif task == "what is your name" or "your name" in task:
                engine = tts.init()
                engine.say("My name is Zira. ")
                engine.runAndWait()
            
            # takes notes for the user 
            elif task == "take notes":
                engine = tts.init()
                engine.say("I'm listening")
                engine.runAndWait()
                # turns the microphone ON
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # stores audio in a variable 'audio'
                    audio = r.listen(source)
                    try:
                        # takes note after converting audio to text 
                        note1 = r.recognize_google(audio)
                        print("You said : {}".format(note1))
                    except:
                        print("Sorry could not recognize what you said")
                        note1 = "No notes"
                engine = tts.init()
                engine.say("Note taken!")
                engine.runAndWait()
            
            # reminds the user about the notes already stored
            elif task == "what were my notes":
                engine = tts.init()
                engine.say("These are the things you asked me to note down for you :")
                engine.say(note1)  # reads the notes out loud
                engine.runAndWait()
                
            elif task == "locate a place":
                address = input("Enter the address: ")
                engine = tts.init()
                engine.say("Locating {}".format(address))
                engine.runAndWait()
                wb.open('https://www.google.com/maps/place/' + address)    

            # download a song using the spotdl module in the ZIRA program
            elif task == "download song" or "download" in task:
                engine = tts.init()
                engine.say("Type the name of the song, artist or album you want to download")
                engine.runAndWait()
                # asks for the name of the song to be downloaded 
                IPpractice.downloadsong()
            
            # terminates the program 
            elif task == "shutdown":
                engine = tts.init()
                engine.say("Okay I'll stop")
                engine.runAndWait()
                ansh = "0"

            elif "where" in task:
                cmd = "whereami predict"   # commands to be run on the command prompt 
                returned_value = subprocess.call(cmd, shell=True)   # runs commands on the Command Prompt
                
            elif task == "mute":
                engine = tts.init()
                engine.say("All systems turning mute")
                engine.runAndWait()
                filepath = "C:/Users/anshc/OneDrive/Documents/ZIRA/mute.bat"
                subprocess.Popen(filepath, shell=True)

            elif task == "unmute":
                filepath = "C:/Users/anshc/OneDrive/Documents/ZIRA/unmute.bat"
                subprocess.Popen(filepath, shell=True)
            
            elif task == "stop":
                engine = tts.init()
                engine.say("Okay I'll stop")
                engine.runAndWait()
                ansh = "0"
                
            elif task[0:19] == "tell me more about ":
                result = wikipedia.summary("{}".format(task[19:]),sentences=3)
                engine = tts.init()
                engine.say(result)
                engine.runAndWait()

            else:
                result = wikipedia.summary("{}".format(task),sentences=1)
                wb.open("https://www.google.com/?#q="+task, new = 2, autoraise = True)
                engine = tts.init()
                engine.say(result)
                engine.runAndWait()
                
