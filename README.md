# Voice-assisted-e-commerce-shopping
A conversational interface that assists with details of products and product comparison with a voice input and output model

## Description  
The project uses **sentence transformers** to convert user-given sentences into embeddings and derive a **cosine similarity** between the sentence query and the available product specifications of the Flipkart website. The embedding with the highest similarity will be displayed on the screen and read aloud using the **pyttsx3** module.

Scraping mechanisms are built from scratch, **BeautifulSoup (bs4)** is used to parse into HTML, and selectors extract meaningful text information. The program iterates through all the available specifications listed for a product and stores them in dictionaries.

**Tkinter** is used to create the app and the UI responsible for getting input and displaying status flags for every possible outcome. 

## Prerequisites
1. Pyttsx3  
   `pip install pyttsx3`
   <br> <br>
2. Tkinter  
   `pip install tk`
   <br> <br>
3. PIL  
   `pip install Pillow`
   <br> <br>
4. BeautifulSoup  
   `pip install beautifulsoup4`
   <br> <br>
5. sentence-transformers  
   `pip install sentence-transformers`
   <br> <br>
6. SpeechRecognition  
   `pip install SpeechRecognition`
   
## Installation

1. Clone the repository locally  
   `git clone https://github.com/keert04/Voice-assisted-e-commerce-shopping/tree/main`
   <br> <br>
2. Navigate inito the repository  
   `cd Voice-assisted-e-commerce-shopping`
   <br> <br>
3. Run app  
   `app.py`

## Usage Instructions:
* Right-click on the voice button to display the menu
* Change the product URL at any time by pasting a new URL in the menu
