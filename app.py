from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.environ.get("GOOGLE_GEMINI_KEY")

client = genai.Client(api_key = api_key)

response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Give me idea of gemini api in 100 words"
)

# print(response.text)
st.markdown(response.text)