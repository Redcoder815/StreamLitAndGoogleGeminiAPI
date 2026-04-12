import streamlit as st

audio_file = st.file_uploader("Upload an audio", type = ["mp3", "ogg", "flac"])

if audio_file:
    st.audio(audio_file)