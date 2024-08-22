import streamlit as st
import random
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui as auto
import Pdata_elements as PD
import time
from winotify import Notification, audio
from translate import Translator
from geopy.geocoders import Nominatim
from geopy import distance

# Bot Name
Bot_Name = "Shri"

# Streamlit setup
st.title("AI Assistant - Shri")
st.sidebar.title("Control Panel")

# Notification Function (Streamlit version)
def notify(messagetoD, mtitle='AI SHRI IS LIVE'):
    st.sidebar.write(f"{mtitle}: {messagetoD}")

# Speaking Function (Using Text instead of Voice for Web)
def speak(audio):
    st.write(audio)

# Initialize the voice engine (Optional for local use)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak_voice(audio):
    engine.say(audio)
    engine.runAndWait()

# Notify the user that the bot is live
messagetoD = f'{Bot_Name} is now able to help you'
notify(messagetoD)

# Function to simulate sending a WhatsApp message
def sendWhatmsg(name, message):
    try:
        if name.upper() in PD.user_list:
            msgToSend = message.replace(' ', '%20')
            webbrowser.open('https://web.whatsapp.com/send?phone=' + PD.user_list.get(name.upper()) + '&text=' + msgToSend)
            speak('Wait for 10 seconds while WhatsApp is loading')
            time.sleep(10)
            auto.hotkey('f11')
            auto.hotkey('enter')
            speak('Message sent successfully')
        else:
            speak('No person named ' + name + ' in contact list')
    except:
        speak("Error occurred while sending the message.")

# Function to calculate distance between two locations
def distancecalc(location1, location2):
    geolocator = Nominatim(user_agent='shri_app')
    try:
        coordinates1 = geolocator.geocode(location1)
        coordinates2 = geolocator.geocode(location2)
        lat1, long1 = coordinates1.latitude, coordinates1.longitude
        lat2, long2 = coordinates2.latitude, coordinates2.longitude
        place1, place2 = (lat1, long1), (lat2, long2)
        dist = distance.distance(place1, place2).km
        speak(f'The distance between {location1} and {location2} is {dist:.2f} km.')
    except:
        speak("Error: The place does not exist.")

# Function to translate text
def translation(msg, language='spanish'):
    translator = Translator(to_lang=language)
    translation = translator.translate(msg)
    return translation

# Streamlit input fields for different commands
command = st.text_input("Enter your command:")

if st.button('Send Command'):
    if 'what is your name' in command.lower():
        speak(f"My name is {Bot_Name}.")
    
    elif 'who built you' in command.lower():
        speak(f"I am {Bot_Name}. And I was built by Aditya Puri.")
    
    elif 'open google' in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    
    elif 'what is the current time' in command.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'send a message' in command.lower():
        name = st.text_input("Enter the contact name:")
        message = st.text_area("Enter your message:")
        if st.button("Send WhatsApp Message"):
            sendWhatmsg(name, message)

    elif 'distance calculation' in command.lower():
        location1 = st.text_input("Enter the first location:")
        location2 = st.text_input("Enter the second location:")
        if st.button("Calculate Distance"):
            distancecalc(location1, location2)
    
    elif 'translate' in command.lower():
        translate_text = st.text_input("Text to Translate:")
        translate_language = st.text_input("Translate to (language):", value="spanish")
        if st.button('Translate'):
            translated_text = translation(translate_text, translate_language)
            speak(f"Translation in {translate_language}: {translated_text}")
            st.write(translated_text)

    elif 'take screenshot' in command.lower():
        auto.screenshot().save("screenshot.png")
        speak("Screenshot taken and saved as screenshot.png")
    
    else:
        speak("I didn't understand the command.")

# Optional Features
# Feel free to add more buttons or text inputs to interact with other functionalities.
