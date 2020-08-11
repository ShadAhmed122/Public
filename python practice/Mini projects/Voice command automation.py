import datetime,pyttsx3,wikipedia,webbrowser,datetime,os
import speech_recognition as sr
chrome_path = r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def iterable(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True


def spek(audio):
    speak=pyttsx3.init("sapi5")
    voice= speak.getProperty('voices')
    speak.setProperty('voice', voice[1].id)
    speak.say(audio)
    speak.runAndWait()
    print(audio)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        spek("Good Morning!")
    elif hour>=12 and hour<18:
        spek("Good Afternoon!")   
    else:
        spek("Good Evening!")  
    spek("I am your Destop Assistant. Sir, tell me how may I help you")  

def takeCommand():
    #It takes microphone input from the user and returns string output
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            # r.pause_threshold = 1
            try:
                audio = r.listen(source)
            except:
                pass
            try:
                text=r.recognize_google(audio,language="en-in").lower()
                print(text)
                return text
            except:
                pass
    except Exception as e:
        print(e)


 

if __name__ == "__main__":
    wishMe()
    while True:
        a=takeCommand()
        if not iterable(a):
            continue

        elif a=="thank you":
            spek("welcome sir")
        
        elif 'open youtube' == a:
            spek("What do you want to search in youtube ,Sir")
            a=takeCommand()
            spek('I\'m opening youtube')
            if a=="nothing":
                webbrowser.get(chrome_path).open("youtube.com")
            else:
                webbrowser.get(chrome_path).open(f"youtube.com/results?search_query={a}")
        

        elif 'open google' == a:
            spek("What do you want to search in google ,Sir")
            a=takeCommand()
            spek('I\'m opening google')
            if a=="nothing":
                webbrowser.get(chrome_path).open("google.com")
            else:
                webbrowser.get(chrome_path).open(f"google.com/search?sxsrf=ALeKk01uhtkBOa71-cF4R9DmFtasOALyPg%3A1594078382050&ei=rrQDX_LhAv6R4-EPk9emyAE&q={a}&oq={a}&gs_lcp=CgZwc3ktYWIQAzICCAAyAggAMgIILjICCAAyAggAMgIIADIECAAQCjICCAAyAggAMgIILjoECAAQQzoHCC4QQxCTAjoGCAAQChBDOgcIABCxAxBDUPo6WNlRYJRZaABwAHgAgAGXAYgB5geSAQMwLjeYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjy8NLd5LnqAhX-yDgGHZOrCRkQ4dUDCAw&uact=5")
            
        
        elif 'open facebook' in a:
            spek('I\'m opening facebook')
            webbrowser.get(chrome_path).open("facebook.com")


        elif a=='shutdown computer':
            spek('computer is shuting down')
            os.system('shutdown /s /t 0')


        elif a=='restart computer':
            spek('computer is restarting')
            os.system('shutdown /r /t 0')


        elif a=='hibernate computer':
            spek('computer is hibernating')
            os.system('shutdown /h /t 0')


        elif 'open vs code' == a:
            spek('I\'m opening Virtual Studio Code')
            os.startfile("D:\program files\Microsoft VS Code\Code.exe")

        elif 'close vs code' == a:
            spek('I\'m closing Virtual Studio Code')
            os.system("TASKKILL /F /IM Code.exe")

        elif 'open pycharm' == a:
            spek('I\'m opening Pycharm')
            os.startfile(r'C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.4\bin\pycharm64.exe')

        elif 'close pycharm' == a:
            spek('I\'m closing Pycharm')
            os.system("TASKKILL /F /IM pycharm64.exe")


        elif 'open chrome' == a:
            spek('I\'m opening Google Chrome')
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif 'close chrome' == a:
            spek('I\'m closing Google Chrome')
            os.system("TASKKILL /IM chrome.exe")


        elif 'what is the time' == a or 'what\'s the time' == a or 'tell me the time'==a:
            spek(str(datetime.datetime.now().strftime("%H:%M:%S")))

        elif 'what is the date' == a or 'what\'s the date' == a or 'tell me the date'==a:
            spek(str(datetime.datetime.now().strftime("%Y-%m-%d")))
        
        elif 'open email' in a:
            spek('I\'m opening emails')
            webbrowser.get(chrome_path).open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        
        elif "search wikipedia" in a:
            try:
                spek("Searching wikipedia")
                a=a.replace("search wikipedia ",'')
                print(a)
                a=wikipedia.summary(a,sentences=2)
                spek(a)
                print(a)
            except Exception as e:
                print(e)
        
        elif 'exit' in a:
            spek("I am exiting ,Sir. Thanks for creating me")
            exit()
            
        else:
            spek(a)   