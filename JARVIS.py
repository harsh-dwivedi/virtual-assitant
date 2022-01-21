from tkinter import *
from  PIL import ImageTk,Image
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import random
import wolframalpha #pip install wolframalpha
import json
import requests
from urllib.request import urlopen
import time


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',160)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def time_():
    Time = datetime.datetime.now().strftime("%I %M %S")
    speak("the current time is....... ")
    speak(Time)

def date_():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is.....")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!...........")
    time_()
    date_()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("good morning sir!........")
    elif hour >=12 and hour<18:
        speak("good afternoon sir!.......")
    elif hour >=18 and hour<24:
        speak("good evening sir!........")
    else:
        speak("good night sir!....")
    
    speak("jarvis at your service. please teel me how can i help you")
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
    
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)
        speak("say that again please")
        return  "None"
        
    return query
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('harshprakash2211@gmail.com','password')
    server.sendmail('harshprakash2211@gmail.com',to,content)
    server.close()
def screenshot():
    img  =pyautogui.screenshot()
    img.save("D:\\Programs\\Python Programs\\Python AI\\Screenshot\\ss.png")
    speak("done sir!.....")
    speak("opening screenshot.....")
    os.startfile("D:\\Programs\\Python Programs\\Python AI\\Screenshot\\ss.png")
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())
    

    
    
class  Widgets:
    def __init__(self):
        root=Tk()
        
        
        root.title('Personal Assistant (J.A.R.V.I.S)')
        root.config(background='red')
        root.geometry("900x900")
        root.iconbitmap("D:\\Programs\\Python Programs\\Python AI\\favicon.ico")
        root.resizable(100,100)

        img=ImageTk.PhotoImage(Image.open(r"D:\\Programs\\Python Programs\\Python AI\\im.png"))
        panel=Label(root,image=img)
        panel.pack(side='right',fill='both',expand='no')

        self.compText=StringVar()
        self.userText=StringVar()

        self.userText.set('click run jarvis to give command')

        userFrame=LabelFrame(root,text="User",font=("Black ops one",10,'bold'))
        userFrame.pack(fill='both',expand='yes')

        left=Message(userFrame,textvariable=self.userText,bg='#21405F',fg='white')
        left.config(font=("Comic Sans MS",24,'bold'))
        left.pack(fill='both',expand='yes')

        compFrame=LabelFrame(root,text='JARVIS',font=('Black ops one',10,'bold'))
        compFrame.pack(fill='both',expand='yes')

        left2=Message(compFrame,textvariable=self.compText,bg='#21405F',fg='white')
        left2.config(font=("Comic Sans MS",24,'bold'))
        left2.pack(fill='both',expand='yes')

        

        btn=Button(root,text='Run JARVIS',font=('Black ops one',10,'bold'),bg='#4B4B4B',fg='white',command=self.clicked).pack(fill='x',expand='no')
        btn2=Button(root,text='CLOSE',font=('Black ops one',10,'bold'),bg='#4B4B4B',fg='white',command=root.destroy ).pack(fill='x',expand='no')
        self.compText.set('Hello I am Jarvis !!! What can i do for you sir?')
        
        root.bind("<Return>",self.clicked) #handle the enter key event of our keyboard
        
        

        root.mainloop()
        
        
    def clicked(self):
        print('working')
        query=takeCommand()
        self.userText.set('listening.........')
        self.userText.set(query)
        query= query.lower()
        
        if 'wikipedia' in query:
            
            query = query.replace("wikipedia","")
            result =wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'singhamit005@gmail.com'
              #  sendEmail(to,content)
                speak(content)
            except Exception as e:
                print(e)
                speak("unable to send the email")
        elif 'open youtube' in query:
            wb.open("youtube.com")
        elif 'open google' in query:
            wb.open("google.com")
        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")
        elif 'logout' in query:
            os.system("shutdown -1") 
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play songs' in query:
            songs_dir= "D:\\Pragrams\\Python Programs\\Python AI\\Music"
            songs = os.listdir(songs_dir)
            # speak('what should i play?')
            speak('select how you want me to play songs....')
            ans = takeCommand()
            while('number' not in ans and ans !='random' and ans !='you choose'):
                speak('i could not understand you . please try again.')
                break
            if 'number' in ans:
                speak('tell me the number')
                n=takeCommand()
                no = int(n)
                os.startfile(os.path.join(songs_dir,songs[no]))
            elif 'random' or 'you choose' in ans:
                no = random.randint(0,11)
                os.startfile(os.path.join(songs_dir,songs[no]))
            else:
                takeCommand()
            
            
        elif 'calculate' in query:
            client = wolframalpha.Client('ET5RP8-LUX4GPA9UH')
            indx = query.lower().split().index('calculate')
            query = query.split()[indx +1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('the answer is :'+answer)
            speak('the answer is :'+answer)
            
            
        elif 'what is' in query or 'who is' in query:
            #use the asme API key that we generated earliear i.e. wolframalpha
            client = wolframalpha.Client('ET5RP8-LUX4GPA9UH')
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("no results")
                
        elif 'thank you' in query.lower():
            speak("Its my pleasure to always help you sir..")


        elif 'sorry' in query.lower():
            speak("well if you really are then say it to my master") 

        elif 'please' in query.lower():
            speak("Don't say please sir!!!... I'm always here to help you")

        elif 'can you sing' in query.lower():
            speak("i can.. but i am  still  learning  new things")  

        elif 'how are you' in query.lower():
            speak("i am always good and ready for help..")     
                
        elif 'what can you do' in query.lower():
            speak("its better if you ask what kind of assistant you are")

        elif'what kind of assistant are you' in query.lower():
            speak("kind of helpful")

        elif'help me'in query.lower():
            speak("always ready to help you sir")

        elif 'what is your name' in query.lower():
            speak("jarvis sir")
            
        elif 'who made you' in query.lower():
            speak("harsh dwivedi... sir!")

        elif 'ok google' in query.lower():
            speak("thats not me sir....i am jarvis")

        elif 'hey siri' in query.lower():
            speak("i am jarvis sir,how can you forget something which is created by you sir") 

        elif 'i want to be rich' in query.lower():
            speak("so do i")         
                
        elif 'remember that' in query:
            speak("what should I remember?")
            data = takeCommand()
            speak("you said me to remember"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query:
            remember =open('data.txt','r')
            speak("you said me to remember that"+remember.read())
            
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("user asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
            
        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3a519cc686844a408f5caf83131aced0")
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top headlines from the buniessindustry')
                print('============TOP HEADLINES================'+'\n')
                for item in data['articles']:
                    if (i<5):
                        print(str(i)+'.'+item['title']+'\n')
                        print(item['description']+'\n')
                        speak(item['title'])
                    else:
                        exit
                    i +=1

            except  Exception as e:
                print(str(e))
        
        
        elif 'screenshot' in query:
            screenshot()
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'open v s code' in query:
            speak('opening v s code........')
            codepath = "C:\\Users\\HARSH DWIVEDI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.exe"
            os.startfile(codepath)
        elif 'notepad' in query:
            speak('opening notepad........')
            ms_word= r"C:\\Windows\\System32\\notepad.exe"
            os.startfile(ms_word)
        
        elif 'stop listening' in query:
            speak('for how many second you wnat me to stop listening your command?')
            ans = int(takeCommand())
            time.sleep(ans)
            print(ans) 
        
        elif 'can you dance' in query:
            speak('yes... but you  cannot  see me')

        elif 'disturb' in query:
            speak('just ignore them...')
        
        elif 'exit' in query:
            speak("pleasure helping you sir!")
            quit()
        
        elif 'close' in query:
            speak("pleasure helping you sir!")
            quit()
                     
        elif 'offline' in query:
            speak("pleasure helping you sir!")
            quit()

if __name__ == "__main__":
    
    speak('jarvis is starting')
    wishme()
    widget=Widgets()