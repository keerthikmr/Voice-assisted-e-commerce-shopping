import pyttsx3
import similarity_matching as sm


def speaker(text):
    engine = pyttsx3.init()

    engine.say(text)

    engine.runAndWait()
