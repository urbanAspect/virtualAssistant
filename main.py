import speech_recognition as sr
import pyttsx3 as speech_to_text
import pywhatkit


listener = sr.Recognizer()
engine = speech_to_text.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except:
        pass
    return command

def run_Jarvis():
    command = take_command()
    if 'jarvis' and 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

# https://www.youtube.com/watch?v=R3XgZ__jQxw poglej za Spotify

run_Jarvis()