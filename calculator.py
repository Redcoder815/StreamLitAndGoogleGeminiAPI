import streamlit as st

num1 = st.number_input("Enter your first number: ", value = None)
num2 = st.number_input("Enter your second number: ", value = None)

selected = st.selectbox("Select your operation", ("+", "-", "*", "/"), index = None)

button = st.button("Calculate")

if button:
    if num1 and num2:
        if selected == "+":
          st.write(f"{num1} + {num2} = {num1 + num2}")
        elif selected == "-":
           st.write(f"{num1} - {num2} = {num1 - num2}")
        elif selected == "*":
           st.write(f"{num1} * {num2} = {num1 * num2}")
        elif selected == "/":
           if num2 != 0:
              st.write(f"{num1} / {num2} = {num1 / num2}")
           else:
              st.error("Cannot divide by zero")

    else:
        st.error("Please enter both numbers")