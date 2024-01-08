import api
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import openai
import locationtest
import data
import Weathertest
import namematch
location = locationtest.get_current_location()

engine = pyttsx3.init('sapi5') # initializing the sapi5 voice engine
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id) # selecting the voice 

def speak(audio):# function to convert text to speech
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hi I am Jarvis.\n How can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        r.pause_thresold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Google Speech Recognition
        print(f"User said: {query}\n")

    except Exception as e:
        #        print(e)
        print("Say that again please")
        query = "Invalid Query"
        #return "None"
    return query

def ai(prompt):
    #key = api.cohereapikey
    import cohere
    co = cohere.Client(api.cohereapikey)

    response = co.chat(
        prompt, 
	    model="command", 
	    temperature=0.9
    )
    answer = response.text
    try:
        print(answer)
        if not os.path.exists("chatlogs"):
            os.mkdir("chatlogs")

        with open(f"chatlogs/{prompt}.txt", "w") as f:
            f.write(answer)

        speak(f"Done Sir\nYou can find the content in the chatlogs directory, in the file chatlogs/{prompt}.txt")

        print(f"Done Sir\nYou can find the content in the chatlogs directory, in the file chatlogs/{prompt}.txt")

    except Exception as e:
        print("Error occurred!!!")
        speak("Sorry sir, I am not able to answer your question at the moment")
    
def chat(prompt):
    import cohere
    co = cohere.Client(api.cohereapikey)

    response = co.chat( 
        prompt, 
	    model="command", 
	    temperature=0.9
    )
    answer = response.text
    return answer

def detail_weather(weather):
    print(f"tempmax {weather['tempmax']}")
    speak(f"tempmax {weather['tempmax']}")
    print(f"tempmin {weather['tempmin']}")
    speak(f"tempmin {weather['tempmin']}")
    print(f"temp {weather['temp']}")
    speak(f"temp {weather['temp']}")
    print(f"feelslike {weather['feelslike']}")
    speak(f"feelslike {weather['feelslike']}")
    print(f"dew {weather['dew']}")
    speak(f"dew {weather['dew']}")
    print(f"humidity {weather['humidity']}")
    speak(f"humidity {weather['humidity']}")
    print(f"precipitation {weather['precip']}")
    speak(f"precipitation {weather['precip']}")
    print(f"description {weather['description']}")
    speak(f"description {weather['description']}")

def openapp(app_index):
    speak(f"Opening {data.apps[app_index][0]} sir")
    os.startfile(data.apps[app_index][1])


if __name__ == "__main__":
        while True:
            query = takeCommand().lower()
            if 'hello' in query:
                wishme()
                while True:
                    query = takeCommand().lower()
                    if 'wikipedia' in query:
                        speak('Searching Wikepedia...')
                        query = query.replace("wikipedia", "")
                        print(query)
                        results = wikipedia.summary(query, sentences=3)
                        speak("According to wikipedia")
                        print(results)
                        speak(results)
                    elif 'write' in query:
                        ai(prompt = query)
                    elif 'the time' in query:
                        speak("the time is")
                        time = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(time)
                    elif 'open website' in query:
                        speak("just say the website which you want to open")
                        website = takeCommand().lower()
                        mw = website.replace(" ", "")
                        speak("Searching...")
                        webbrowser.open("https://www."+mw+".com")
                    elif 'play music from web' in query:
                        speak("Playing music from youtube music sir")
                        music_index = random.randint(0, len(data.music_links)-1)
                        speak(f"Playing {data.music_links[music_index][0]} from youtube music")
                        webbrowser.open(data.music_links[music_index][1])
                    elif query == 'play music' in query:
                        music_dir = 'D:\Music'
                        songs = os.listdir(music_dir)
                        print(songs)
                        speak("playing music sir")
                        os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))
                    elif 'open code' in query:
                        openapp(0)
                    elif 'open vs code' in query:
                        openapp(0)
                    elif 'open any desk' in query:
                        openapp(1)
                    elif 'open word' in query:
                        openapp(2)
                    elif 'open excel' in query:
                        openapp(3)
                    elif 'open powerpoint' in query:
                        openapp(4)
                    elif 'my location' in query:
                        print(location)
                        print("Current Location:")
                        speak("Sir, Your Current Location is")
                        print("Latitude:", location.latlng[0])
                        speak(f"Latitude {location.latlng[0]}")
                        print("Longitude:", location.latlng[1])
                        speak(f"Longitude {location.latlng[1]}")
                        print("City:", location.city)
                        speak(f"City {location.city}")
                        print("State:", location.state)
                        speak(f"State {location.state}")
                        print("Country:", location.country+"DIA")
                        speak(f"Country {location.country}+DIA")
                    elif 'longtitude' in query:
                        print("Longitude:", location.latlng[1])
                        speak(f"Sir your Longitude is {location.latlng[1]}")
                        print("Latitude:", location.latlng[0])
                        speak(f"and Latitude {location.latlng[0]}")
                    elif 'latitude' in query:
                        print("Latitude:", location.latlng[0])
                        speak(f"Sir your Latitude is {location.latlng[0]}")
                        print("Longitude:", location.latlng[1])
                        speak(f"and Longitude {location.latlng[1]}")
                    elif "today's weather" in query:
                        weather = Weathertest.jsonData['days'][0]
                        detail_weather(weather=weather)
                    elif "tomorrow's weather" in query:
                        weather = Weathertest.jsonData['days'][1]
                        detail_weather(weather=weather)
                    elif 'temperature' in query:
                        weather = Weathertest.jsonData['days'][0]
                        print("Temperature:", weather['temp'])
                        speak(f"Sir, the temperature is {weather['temp']}")
                        print("Max_Temperature:", weather['tempmax'])
                        speak(f"max temperature {weather['tempmax']}")
                        print("Min_Temperature:", weather['tempmin'])
                        speak(f"min temperature {weather['tempmin']}")
                        print(f"Feelslike {weather['feelslike']}")
                        speak(f"and Feelslike {weather['feelslike']}")
                    elif 'send email' in query:
                        try:
                            speak("To whom should I sent this mail")
                            to = takeCommand().lower()
                            index = namematch.match(to)
                            print(index)
                            if(namematch.match(to) == -1):
                                speak("Please try again by saying send email")
                            else:
                                speak("What should I say?")
                                content = takeCommand().lower()
                                if(content == None):
                                    speak("Say that again")
                                    content = takeCommand().lower()
                                else:
                                    content = content
                                print(content)
                                print("Sending Email")
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.ehlo()
                                server.starttls()
                                server.login('palshubho2020@gmail.com', api.mailpasskey)
                                server.sendmail('palshubho2020@gmail.com', data.contacts[index][1], content)
                                server.close()
                                speak("Email has been sent")
                        except Exception as e:
                            print(e)
                            speak("Sorry Sir, I am not able to send this email")
                    elif query == 'lights on' or query == 'turn on lights' or query == 'turn on the lights' or query == 'turn on the light' or query == 'turn on the lights':
                        # sender.py
                        import reciver
                        reciver.process_data("97")
                    elif query == 'lights off' or query == 'turn off lights' or query == 'turn off the lights' or query == 'turn off the light' or query == 'turn off the lights':
                        # sender.py
                        import reciver
                        reciver.process_data("1")
                    elif 'current affairs' in query:
                        import testnewstwo
                    elif 'quit' in query:
                        exit()
                    elif query == "Invalid Query":
                        speak("Sorry Sir, I didn't get you")
                    else:
                        if query != "Invalid Query":
                            print(query)
                            ans=chat(prompt=query)
                            print(ans)
                            speak(ans)
                    