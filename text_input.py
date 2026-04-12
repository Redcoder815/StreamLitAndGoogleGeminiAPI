import streamlit as st

st.write("Hello world")

st.title("Streamlit tile", anchor = False)

st.header("content header", divider = True)
st.subheader("content subheader")
st.text("This is a text")

st.markdown(":red[**Hello**] *World*")
st.markdown(":orange-background[:red[**Hello**] *World* :world_map:]")

a = 20
b = 50

st.write(a, b)