import streamlit as st

user_text = st.text_input("Enter some text")

if user_text:
    st.title(user_text)
    st.divider()
    st.header(user_text)
    st.divider()
    st.subheader(user_text)
    st.divider()
    st.text(user_text)