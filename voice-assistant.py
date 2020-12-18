import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bot' in command:
                command = command.replace('bot', '')
                print(command)
    except:
        pass
    return command


def run_bot():
    command = take_command()
    print(command)
    if 'hello' in command:
        talk('Hey!! nice to meet you!')
    elif 'how are you' in command:
        talk('I am fine! have a good day!')
    elif 'thanks' in command:
        talk("You're welcome")
    elif 'ok' in command:
        talk('sure!')
    elif 'what is your name' in command:
        talk('My name is bot. I am personal voice assistant of Avishek Dutta. I was developed by him!')
    elif 'who are you' in command:
        talk('My name is bot. I am personal voice assistant of Avishek Dutta. I was developed by him!')
    elif 'what are you doing' in command:
        talk('I am talking with you!!')
    elif 'just shut up' in command:
        talk('Mind your language!!')
    elif 'shut up' in command:
        talk('Mind your language!!')
    elif 'just joking' in command:
        talk("it's okay!!")
    elif 'sorry' in command:
        talk('Ooooh!! okay!!')
    elif 'be careful' in command:
        talk('be careful!!')
    elif 'bangladesh' in command:
        wiki = wikipedia.summary("Bangladesh", sentences=1)
        talk(wiki)
    elif 'facebook' in command:
        wiki = wikipedia.summary("Facebook", sentences=1)
        talk(wiki)
    elif 'python' in command:
        wiki = wikipedia.summary("Python", sentences=1)
        talk(wiki)
    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    else:
        talk('Please say the command again.')


while True:
    run_bot()