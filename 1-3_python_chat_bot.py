import speech_recognition as sr
import pyttsx3

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

# Initialize the recognizer
r = sr.Recognizer()
validAudio = False
i = 0
attempts = 3
audio = False

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Use the microphone as source for input
with sr.Microphone() as source:
    
    # You should hear your Personal Assistant say the following:
    SpeakText("Hello there! I am Python Chat Bot. You can call me PeeCeeBee.")
    
    # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
    print("PeeCeeBee is now listening.....")
    r.adjust_for_ambient_noise(source, duration=1)
    
    # You should now here your Personal Assistance ask for your name
    SpeakText("What is your name?")

    while i < attempts:        
        
        # Counting up the attempts
        i += 1
        
        # Listen for the user's input
        # We are introducing a timeout after which the bot will stop listening each time
        # Note a timeout will cause an error called WaitTimeoutError which we need to catch
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            validAudio = False
        
        # If there is audio (i.e. not timed out)
        if audio:
        
            # Check if the audio is recognisable
            try:
                # Using google to recognize audio
                name = r.recognize_google(audio)
                validAudio = True
            except sr.UnknownValueError:
                print("Could not understand audio....")
                validAudio = False
            except sr.RequestError as e:
                print("Recog Error; {0}".format(e))
                break
            
            # If audio is recognised...
            if validAudio == True: 
                
                name = "'" + name + "'"
                print(name)
                
                # Using the Natural Language Toolkit we will select someone's name from any sentence they may reply with
                # For example: "Hello there yourself. How are you? My name is Mickey Mouse"
                try:
                    nltk_results = ne_chunk(pos_tag(word_tokenize(name)))
                    
                    for nltk_result in nltk_results:
                        if type(nltk_result) == Tree:
                            nameFound = ''
                            for nltk_result_leaf in nltk_result.leaves():
                                nameFound += nltk_result_leaf[0] + ' '
                    print("Hi " + nameFound +  "!")
                    SpeakText("It is nice to meet you " + nameFound)
                    break
                except:
                    SpeakText("Sorry, I don't think you mentioned your name. Please try again.")
                
            # If audio is not recognised...
            elif validAudio == False and i < attempts:
                SpeakText("Sorry. I did not quite understand that. Please try again.")
        
        # If there is no audio after the timeout period
        elif not audio and i < attempts:
            print("Timed out....")
            SpeakText("Sorry. I did not hear you. Please try again.")
    
    # No more attempts....
    else:
        print("No more attempts....")
        SpeakText("Sorry. There seems to be a problem. Good bye.")

