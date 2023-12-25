import pyttsx3
import similarity_matching as sm

def speaker(specificaion):
    engine = pyttsx3.init()
    
    specification_name = specificaion[0]
    specification_detail = specificaion[1]
    
    if (specification_name == '0'):
        text = "Sorry, I could not find the specification you were looking for."
        # Display in UI

    else:
        text = f"The {specification_name} is {specification_detail}"
        # Display in UI
        
    engine.say(text)

    engine.runAndWait()
