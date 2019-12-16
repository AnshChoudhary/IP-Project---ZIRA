import datetime
import pyttsx3 as tts

# wishes the user as per the time in that specific timezone
def wishMe():
    
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
      engine = tts.init()
      engine.say("Good Morning!")
      engine.runAndWait()



    elif hour>=12 and hour<18:
      engine = tts.init()
      engine.say("Good Afternoon!")
      engine.runAndWait()
      

    else:
      engine = tts.init()
      engine.say("Good Evening!")
      engine.runAndWait()


