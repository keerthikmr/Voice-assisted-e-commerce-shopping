import speech_recognition as sr

def recognize_speech():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        print(text)

    except sr.UnknownValueError:
        print("Could not recognize what you said. Please try again.")

if __name__ == "__main__":
    recognize_speech()
