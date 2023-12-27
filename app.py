from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import scrape
import similarity_matching
from speak import speaker


# Adds "listening" status
def update_listen():
    text_label_update("Listening...")
    speaker("listening")


# Adds "recognizing" status
def update_recognize():
    text_label_update("Recognizing...")
    speaker("recognizing")


# Repositions the window after every text label update
# Helps in adjusting the label size according to the text
def position_window(window_width, window_height):
    x = screen_width - window_width - 5
    y = screen_height - window_height - 5

    window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

    # Reposition the button after change in size of window and label
    # Applies grid and pushes the button to the right
    voice_button.update()


# Updates label to display the final result of the query
def result_display(text):
    text_label_update(text)

    # Fetches a list of specification name and corresponding detail
    specification = similarity_matching.main(text, detail_dict)

    if specification[0] != "0":
        text = f"{specification[0]}: {specification[1]}"

        # Limits the length of the text to be displayed on label
        if len(text) > 120:
            text = text[:115] + "..."

    # Similarity matching returns '0' if no match is found
    else:
        text = "No match found."
        text_label.config(foreground="red")

    text_label_update(text)

    # Reads the resulting text
    speaker(text)


# Updates label to display the current status of the assistant
def text_label_update(text):
    text_label.config(text=text)

    # Adjusts the width of the label according to the text and adds width of the button to give space
    label_width = text_label.winfo_reqwidth() + 52

    # Repositions window to fit new label width
    position_window(label_width, 55)

    # Positions the label to the left of voice button
    text_label.grid(row=0, column=0)
    text_label.update()


# Recognizes speech and returns the text
def recognize_speech():
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        try:
            recognizer.adjust_for_ambient_noise(source)
            # Display "listening" in label
            update_listen()
            audio_data = recognizer.listen(source, timeout=5)

        except sr.WaitTimeoutError:
            # For use in displaying "no speech detected" in label
            return 1

        except Exception as e:
            # For use in displaying "could not recognize your voice" in label
            return None

    try:
        # Display "recognizing" in label
        update_recognize()
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        return text

    except Exception as e:
        return None


# Called when voice button is pressed
def recognize():
    global url_accept
    if url_accept == False:
        # Open selector window, prompt for URL
        selector_window(e=None)

    else:
        # Ensures text color is black even if previous text was red
        text_label.config(foreground="black")

        text = recognize_speech()

        if text == None:
            text = "Could not recognize your voice."
            text_label.config(foreground="red")
            text_label_update(text)
            speaker(text)

        elif text == 1:
            text = "No speech detected."
            text_label.config(foreground="red")
            text_label_update(text)
            speaker(text)

        elif len(text) > 120:
            text = "Request too long."
            text_label.config(foreground="red")
            text_label_update(text)
            speaker(text)

        else:
            result_display(text)


# Called when submit button is pressed
def url_get():
    url = url_entry.get("1.0", END)

    # Reset entry box after getting URL
    url_entry.delete("1.0", END)

    global detail_dict

    # Extracts information from the URL in {specification type : detail} format
    detail_dict = scrape.extract_information(url)

    # For displaying status of URL action
    inform_label.pack(side=BOTTOM, pady=10)

    if detail_dict == 1:
        inform_label.config(text="Problem with the URL. Try again.")

    elif detail_dict == 2:
        inform_label.config(text="Too many requests. Try again later.")

    else:
        global url_accept

        # Next voice button click shuold accept voice input
        url_accept = True
        voice_button.config(background="green")
        select_window.destroy()
        speaker("Ready for input")


# Called when right click is pressed on voice button or url_accept is not true
def selector_window(e):
    global url_entry
    global select_window
    global inform_label

    select_window = Tk()

    select_window.title("Selector")
    select_window.geometry("300x240")

    url_label = Label(select_window, text="Paste the flipkart URL here")

    url_entry = Text(select_window, width=35)

    clear_button = Button(
        select_window, text="Clear", command=lambda: url_entry.delete(1.0, END)
    )

    submit_button = Button(select_window, text="Submit", command=url_get)

    close_button = Button(select_window, text="Close Assistant", command=close_window)

    inform_label = Label(select_window, text="", foreground="red")

    url_label.place(y=20, x=65)
    url_entry.place(x=7.5, y=60, height=50)
    clear_button.place(y=110, x=230)
    submit_button.place(y=130, x=110)
    close_button.place(y=170, x=80)
    select_window.mainloop()


# Called when close button is pressed, exits the program
def close_window():
    window.destroy()
    select_window.destroy()


# To check if URL is valid and if data is extracted
url_accept = False

# Holds the information extracted from the URL
detail_dict = {}

window = Tk()

window.title("Shopping assistant")

# For positioning the window in the bottom right corner
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 55
window_height = 55

# Removes the title bar
window.overrideredirect(True)

button_img = Image.open("Assets/voice_button.png")
button_img = button_img.resize((50, 50), Image.ANTIALIAS)
button_img = ImageTk.PhotoImage(button_img, master=window)

voice_button = Button(
    window, image=button_img, height=50, width=50, background="red", command=recognize
)
voice_button.grid(row=0, column=1)

# Right click to change URL or open UI
voice_button.bind("<Button-3>", selector_window)

text_label = Label(window, wraplength=400, padx=10)

position_window(window_width, window_height)

window.mainloop()
