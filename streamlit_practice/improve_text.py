from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.environ.get("GOOGLE_GEMINI_KEY")

client = genai.Client(api_key = api_key)

text = st.text_input("Input text to improve")

button = st.button("Submit")

if button:
    full_prompt = f"Improve this sentence professionally: {text}"
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = full_prompt
    )
    st.markdown(response.text)



# # app3_sentence_improver.py
# import os
# import streamlit as st
# from google import genai

# st.title("Professional Sentence Improver")

# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     st.error("GEMINI_API_KEY not found. Please set your API key first.")
#     st.stop()

# client = genai.Client(api_key=api_key)

# sentence = st.text_area("Enter a sentence")

# if st.button("Improve Professionally"):
#     if not sentence.strip():
#         st.warning("Please enter a sentence.")
#     else:
#         try:
#             full_prompt = f'''
# Improve this sentence professionally.

# Sentence: "{sentence}"

# Only return the improved sentence.
# '''
#             response = client.models.generate_content(
#                 model="gemini-3-flash-preview",
#                 contents=full_prompt
#             )

#             st.subheader("Improved Version")
#             st.write(response.text)

#         except Exception as e:
#             st.error(f"Error: {e}")
