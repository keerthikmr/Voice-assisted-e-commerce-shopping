import speech_recognition as sr

def recognize_speech():

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        print(text)
        return text
    
    except sr.UnknownValueError:
        return None
