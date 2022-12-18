import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Use the microphone as source for input
with sr.Microphone() as source:
    
    # You should hear your Personal Assistant say the following:
    SpeakText("Hello there! What is your name?")
    
    # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source, duration=1)

    # Listen for the user's input
    audio = r.listen(source)

    # Using google to recognize audio
    name = r.recognize_google(audio)

    print("Hi " + name +  "!")
    
    SpeakText("It is nice to meet you " + name)
