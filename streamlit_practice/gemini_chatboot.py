from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.environ.get("GOOGLE_GEMINI_KEY")

client = genai.Client(api_key = api_key)

text = st.text_input("Ask a question")

button = st.button("Submit")

if button:
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = text
    )
    st.markdown(response.text)