from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import scrape
import similarity_matching
from speak import speaker


def update_listen():
    text_label_update("Listening...")
    speaker("listening")


def update_recognize():
    text_label_update("Recognizing...")
    speaker("recognizing")


def position_window(window_width, window_height):
    x = screen_width - window_width - 5
    y = screen_height - window_height - 5

    window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    voice_button.update()


def result_display(text):
    text_label_update(text)
    specification = similarity_matching.main(text, detail_dict)
            
    if specification[0] != '0':
        text = f"{specification[0]}: {specification[1]}"
        if (len(text) > 120):
            text = text[:115] + "..."
    else:
        text = "No match found."
        text_label.config(foreground="red")

    text_label_update(text)
    speaker(text)


def text_label_update(text):
    text_label.config(text=text)
    
    label_width = text_label.winfo_reqwidth() + 52

    position_window(label_width, 55)

    text_label.grid(row=0, column=0)
    text_label.update()


def recognize_speech():
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        try:
            recognizer.adjust_for_ambient_noise(source)
            update_listen()
            audio_data = recognizer.listen(source, timeout=5)

        except sr.WaitTimeoutError:
            return 1
        
        except Exception as e:
            return None

    try:
        # Recognize speech using Google Speech Recognition
        update_recognize()
        text = recognizer.recognize_google(audio_data)
        return text
    
    except Exception as e:
            return None
    

def recognize():
    global url_accept
    if(url_accept == False):
        selector_window(e=None)
    
    else:
        text = recognize_speech()
        text_label.config(foreground="black")

        if (text == None):
            text = "Could not recognize your voice."
            text_label.config(foreground="red")
            text_label_update(text)
            speaker(text)
        
        elif(text == 1):
            text = "No speech detected."
            text_label.config(foreground="red")
            text_label_update(text)
            speaker(text)

        elif(len(text) > 120):
            text = "Request too long."
            text_label.config(foreground="red")
            text_label_update(text)
            speaker(text)
        
        else:
            result_display(text)


def url_get():
    url = url_entry.get("1.0", END)
    url_entry.delete("1.0", END)

    global detail_dict
    detail_dict = scrape.extract_information(url)
    
    inform_label.pack(side=BOTTOM, pady=10)

    if detail_dict == 1:
        inform_label.config(text="Problem with the URL. Try again.")

    elif detail_dict == 2:  
        inform_label.config(text="Too many requests. Try again later.")

    else:
        global url_accept

        url_accept = True
        voice_button.config(background="green")
        select_window.destroy()


def selector_window(e):
    global url_entry
    global select_window
    global inform_label

    select_window = Tk()

    select_window.title("Selector")
    select_window.geometry("300x240")

    url_label = Label(select_window, text="Paste the flipkart URL here")
    url_entry = Text(select_window, width=35)

    clear_button = Button(select_window, text="Clear", command=lambda: url_entry.delete(1.0, END))
    
    submit_button = Button(select_window, text="Submit", command=url_get)

    close_button = Button(select_window, text="Close Assistant", command=close_window)

    inform_label = Label(select_window, text="", foreground="red")

    url_label.place(y=20, x=65)
    url_entry.place(x=7.5, y=60, height=50)
    clear_button.place(y=110, x=230)
    submit_button.place(y=130, x=110)
    close_button.place(y=170, x=80)
    select_window.mainloop()


def close_window():
    window.destroy()
    select_window.destroy()


url_accept = False
detail_dict = {}

window = Tk()

window.title("Shopping assistant")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 55
window_height = 55

window.overrideredirect(True)

button_img = Image.open("Assets/voice_button.png")
button_img = button_img.resize((50, 50), Image.ANTIALIAS)
button_img = ImageTk.PhotoImage(button_img, master=window)

voice_button = Button(window, image=button_img, height=50, width=50, background="red", command=recognize)
voice_button.grid(row=0, column=1)
voice_button.bind("<Button-3>", selector_window)

text_label = Label(window, wraplength=400, padx=10)

position_window(window_width, window_height)

window.mainloop()
