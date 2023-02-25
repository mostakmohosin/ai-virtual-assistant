import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
from email.message import EmailMessage
import smtplib

# Speech engine initialisation
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 = male, 1 = female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant. What can I do for you?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
    
        print("Say that again please...")  
        return "None"
    return query

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Your email address', 'app password')
    email = EmailMessage()
    email['From'] = 'Your email address'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

#List of gmails
email_list = {
    "friend a": "a1@gmail.com",
    "friend b": "b1@gmail.com",
    "friend c": "c1@gmail.com"
}
# Main loop
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'send an email' in query:
            try:
                speak('To Whom you want to send email')
                name = takeCommand()
                receiver = email_list[name]
                print(receiver)
                speak('What is the subject of your email?')
                subject = takeCommand()
                speak('Tell me the text in your email')
                message = takeCommand()
                send_email(receiver, subject, message)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,I am not able to send this email")  

        elif 'tata'or'goodbye'or'bye'or'exit' in query:
                speak('Goodbye, Thank you for using me. See you again')
                break
        

#mostak mohosin-2023
