import speech_recognition as sr
import smtplib
import pyttsx3
import easyimap as e
from email.message import EmailMessage
unm="****@gmail.com"
pwd="****"

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str="Speak Now:"
        speak(str)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            return text
        except:
            str="Sorry could not recognize what you said"
            speak(str)
def sendmail():
    rec="jananiu2907@gmail.com"
    str="Please speak the body of your email"
    speak(str)
    msg=listen()
    str="You have spoken the message"
    speak(str)
    speak(msg)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(unm,pwd)
    server.sendmail(unm,rec,msg)
    server.quit()
    str="The email has been sent"
    speak(str)
def readmail():
    server=e.connect("imap.gmail.com",unm,pwd)
    server.listids()
    str="Please say the Serial Number of the email you want to read starting from the latest"
    speak(str)
    a=listen()
    if(a=="Tu"):
        a="2"
    b=int(a)-1
    email=server.mail(server.listids()[b])
    str="The email is from: "
    speak[str]
    speak(email.title)
    str="The body of the mail is: "
    speak(str)
    talk(email.body)
str="welcome to voice controlled email service"
speak(str)
while(1):
    str="What do you want to do?"
    speak(str)
    str="speak SEND to send email  speak READ  to read inbox  speak EXITV to exit"
    speak(str)
    ch=listen()
    if(ch=="send"):
        str="You have chosen to send an email"
        speak(str)
        sendmail()
    elif(ch=="read"):
        speak = "You have chosen to read email"
        talk(str)
        readmail()
    elif(ch=="exit"):
        str = "You have chosen to exit.Bye!!"
        speak(str)
        exit(1)
    else:
        print("Invalid choice!!")
        speak(str)
        speak(ch)