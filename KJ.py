import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import requests

#printing loading messeage
print('Loading your assistant -KILLJOY ')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2.0)
        print("Speak now .....")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry,say that again")
            return "None"
        return statement

speak("Loading your personal assistant KILLJOY")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "good bye" in statement or "okbye" in statement or "top" in statement:
            speak('Call me again if you need any help have a good day')
            print('Call me again if you need any help have a good day')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        
        elif 'check my attendance' in statement:
            webbrowser.open_new_tab("https://s.amizone.net/")
            speak("amizone is open now")
            time.sleep(5)
        elif 'order food' in statement:
            webbrowser.open_new_tab("https://www.zomato.com/")
            speak("amizone is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        
        

        elif 'open chrome' in statement:
            os.startfile("chrome.exe")
            speak("Chrome Opend")
            time.sleep(5)

        elif 'close chrome' in statement:
            os.system("taskkill /im chrome.exe /f")
            speak("Chrome Closed")
            time.sleep(5)




        elif 'open notepad' in statement:
            os.startfile("notepad.exe")
            speak("notepad Opend")
            time.sleep(5)



        elif 'close notepad' in statement:
            os.system("taskkill /im notepad.exe /f")
            speak("notepad Closed")
            time.sleep(5)            
        
    
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open teams' in statement:
            webbrowser.open_new_tab("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=110ab703-c0ed-47be-9317-d4e2fca98671&client-request-id=3fdbe98e-be5c-4ad5-bafe-f5e6cde6f456&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=d659239e-7549-46b1-9b01-55644a1acc4c&domain_hint=&sso_reload=true")
            speak("Microsoft Teams is open now")
            time.sleep(5)

        elif 'open my playlist' in statement:
            webbrowser.open_new_tab("https://youtube.com/playlist?list=PLilRiTj9Nq3u6JsAu3sOEx4Pq2O5-6qF3")
            speak("Enjoy your playlist")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name+"&units=metric"
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in Celsius is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement or 'tell me about you' in statement:
            speak('I am KILLJOY your  persoanl assistant you can call me kj. I am programmed to help you in makeing your life work eassy '
                  ' I can open youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too'
                  'any thing withing my boundries i can help you ')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Priyanshu Banerjee as a minor project for his colleage work but I am capable of more than just that")
            print("I was built by Priyanshu Banerjee as a minor project for his colleage work but I am capable of more than just that")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)


        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'hey killjoy' in statement or 'hey kj' in statement or 'killjoy' in statement or 'kj' in statement:
            speak('I can answer to any questions you want')
            question=takeCommand()
            app_id="PYQL7H-GJVLRJKLT4"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement or "shutdown" in statement  or "signout" in statement  or "logoff" in statement  or "shut down" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)












