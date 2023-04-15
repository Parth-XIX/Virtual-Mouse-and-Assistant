import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir")
    elif hour > 12 and hour < 18:
        speak("Good Evening Sir")
    elif hour >= 18 and hour > 0:
        speak("Good Night")
    print("I am unknown, how may i help you")
    speak("I am unknown, how may i help you")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:

        print("Please say again...")
        return "none"
    return query


def taskexecution():
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")


if __name__ == "main":
   taskexecution()
