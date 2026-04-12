import streamlit as st

image = st.file_uploader("Upload an image", type = ["jpg", "jpeg", "png"], accept_multiple_files = True)

print(type(image))

if image:
    col = st.columns(len(image))
    for i, img in enumerate(image):
        with col[i]:
            st.image(img)