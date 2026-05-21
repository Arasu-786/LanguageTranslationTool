import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

# Translator object
translator = Translator()

# Page config
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title(" AI Language Translation Tool")
st.write("Translate text into multiple languages instantly.")

# User input
text = st.text_area("Enter Text to Translate")

# Language list
language_names = list(LANGUAGES.values())

# Source language
source_lang = st.selectbox(
    "Select Source Language",
    language_names
)

# Target language
target_lang = st.selectbox(
    "Select Target Language",
    language_names
)

# Convert language names to language codes
source_code = list(LANGUAGES.keys())[
    list(LANGUAGES.values()).index(source_lang)
]

target_code = list(LANGUAGES.keys())[
    list(LANGUAGES.values()).index(target_lang)
]

# Translate button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        try:
            # Translation
            translated = translator.translate(
                text,
                src=source_code,
                dest=target_code
            )

            translated_text = translated.text

            st.success("Translation Successful ")

            # Show translated text
            st.subheader("Translated Text")
            st.write(translated_text)

            # Copy feature
            st.code(translated_text, language=None)

            # Text to Speech
            tts = gTTS(
                text=translated_text,
                lang=target_code
            )

            audio_file = "translated_audio.mp3"
            tts.save(audio_file)

            # Audio player
            audio_bytes = open(audio_file, "rb").read()

            st.audio(audio_bytes, format="audio/mp3")

            # Download audio button
            with open(audio_file, "rb") as file:
                st.download_button(
                    label="⬇ Download Audio",
                    data=file,
                    file_name="translated_audio.mp3",
                    mime="audio/mp3"
                )

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Developed using Python, Streamlit, Google Translate API, and gTTS")