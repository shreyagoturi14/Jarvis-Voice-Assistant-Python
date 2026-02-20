import speech_recognition as sr
import webbrowser
import pyttsx3 #it helps to convert text to speech
import music


#pip install pocketsphnix
recognizer=sr.Recognizer()
engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    print(c)
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music.music[song]
        webbrowser.open(link)

if __name__=="__main__":
    speak("initializing voice assistant")
    while True:
    #    listen for the wake "Hello"
    #    obtain audio from the microphone
       r=sr.Recognizer()
    
        
        
       print("recognizing.....")
       try:
          with sr.Microphone()as source:
            print("Listening...")
            audio=r.listen(source,timeout=2,phrase_time_limit=1)
    
          word=r.recognize_google(audio)
          if(word.lower()=="Jarvis"):
            
            speak("yes i'm listing")
            
            #listen for command
            with sr.Microphone() as source:
                print("jarvis Active")
                audio=r.listen(source)
                command=r.recognize_google(audio)
                
                processCommand(command)
                
       except Exception as e:
            print("Error;".format(e))