import streamlit as st

name = st.text_input("Enter your name")
st.write("Hello", name)
print(type(name))

age = st.number_input("Enter your age: ",value = None)
st.write("Your age is ", age)

pressed = st.button("submit")

if pressed:
    st.write(f"{name} and {age}")

selected = st.selectbox("Select your country", ("Bangladesh", "India"), index = None, accept_new_options = True)

print(type(selected))

st.write("You selected ", selected)