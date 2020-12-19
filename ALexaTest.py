import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 0.7)
#engine.say("Hello Irfan")
#engine.say("I'm your assistant,alexa")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Speak now...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #command = command.lower()
            if 'alexa' in command:
                talk(command)

    except:
        pass
    return command

#take_command()


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print('playing...')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'who is' in command:
        human = command.replace('who is','')
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'what is your name' in command:
        talk('My name is Alexa,your assistant')

    elif 'Turn off' in command:
        talk('Turning off..')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('please say the command again.')

while True:
   run_alexa()
