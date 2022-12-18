import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
validAudio = False
i = 0
attempts = 3

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Use the microphone as source for input
with sr.Microphone() as source:
    
    # You should hear your Personal Assistant say the following:
    SpeakText("Hello there! I am Python Chat Bot. You can call me PeeCeeBee.")
    
    # Wait for a second to let the recognizer adjust the energy threshold
    # based on the surrounding noise level
    print("PeeCeeBee is now listening.....")
    r.adjust_for_ambient_noise(source, duration=1)
    
    # You should now hear your Personal Assistance ask for your name
    SpeakText("What is your name?")

    while i < attempts:        

        # Counting up the attempts
        i += 1
        
        # Listen for the user's input
        audio = r.listen(source)
        
        # Check if the audio is recognisable
        try:
            # Using google to recognize audio
            name = r.recognize_google(audio)
            validAudio = True
        except sr.UnknownValueError:
            print("Could not understand audio")
            validAudio = False
        except sr.RequestError as e:
            print("Recog Error; {0}".format(e))
            break
        
        # If audio is recognised...
        if validAudio == True: 
            print("Hi " + name +  "!")
            SpeakText("It is nice to meet you " + name)
            break
        # If audio is not recognised...
        elif validAudio == False and i < attempts:
            SpeakText("Sorry. I did not quite understand that. Please try again.")
    
    # No more attempts....
    else:
        SpeakText("Sorry. There seems to be a problem. Good bye.")