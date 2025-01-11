from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os


GOOGLE_API_KEY = "AIzaSyDlGuiJOqQePVsQEu5gWiftb74RDGvcq-c"
llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp" , api_key=GOOGLE_API_KEY)



def handle_audio_input():
    recognizer = sr.Recognizer()
    
    # Listen for audio input
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        audio = recognizer.listen(source)
    
    try:
        text_input = recognizer.recognize_google(audio)
        st.success(f"Your text: {text_input}")
        
        # Simulate AI response (replace with actual LLM logic)
        with st.spinner("AI Responding..."):
            response = llm.invoke(text_input)  # Replace with actual LLM logic
            response = str(response.content)  # Ensure response is a string
            
            if response:
                # Generate and play audio response
                tts = gTTS(text=response, lang='en' ,tld='com')
                audio_file = "response.mp3"
                tts.save(audio_file)
                
                # Display audio for playback
                st.audio(audio_file, format="audio/mp3")
                
                # Optionally clean up the generated file
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand that.")
    except sr.RequestError:
        st.error("Sorry, the speech recognition service is unavailable.")

# Streamlit App
st.title("Voice-Enabled Chatbot with Audio Response")

# Button to start listening
if st.button("Start Speaking"):
    with st.spinner("Listening..."):
        handle_audio_input()
