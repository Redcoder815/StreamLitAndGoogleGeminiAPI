import streamlit as st

name = st.text_input("Enter your name")

age = st.number_input("Age")

selected = st.selectbox("Select your job", ("Teacher", "Student", "Doctor"), index = None, accept_new_options = True)

pressed = st.button("Submit")

if pressed:
    if name and age and selected:
        st.write(f"Your name is {name}, your age is {age} and your job is {selected}")
        st.success("Information submitted successfully")
    else:
        st.warning("Please fill all the fields")