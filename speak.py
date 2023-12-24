import pyttsx3
# from similarity_matching import specification_name, specification_detail
import similarity_matching as sm

def speaker(text):
    engine = pyttsx3.init()
    
    engine.say(text)

    engine.runAndWait()


# if __name__ == "__main__":
    
#     if (sm.specification_name == '0'):
#         speak("Sorry, I could not find the specification you were looking for.")
    
#     else:
#         speak(f"The {sm.specification_name} is {sm.specification_detail}")
