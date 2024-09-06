import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# List all available microphones and prompt user to select one
print("Available Microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone {index}: {name}")

# Prompt user to choose a microphone by index
mic_index = int(input("Enter the microphone index you want to use: "))

# Infinite loop for the user to speak
while True:
    try:
        print("Adjusting for ambient noise...")
        # Use the selected microphone as the source for input
        with sr.Microphone(device_index=mic_index) as source2:
            # Adjust for ambient noise for better accuracy
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Listening...")
            # Listen to the user's input
            audio2 = r.listen(source2)

            print("Processing audio...")
            # Use Google Speech Recognition to convert audio to text in the specified language
            MyText = r.recognize_google(audio2, language='hi-IN')
            MyText = MyText.lower()

            print(f"You said: {MyText}")
            # Speak the recognized text
            SpeakText(MyText)

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
