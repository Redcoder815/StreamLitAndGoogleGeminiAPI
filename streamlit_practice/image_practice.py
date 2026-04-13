import streamlit as st

image = st.file_uploader("Upload an image", type = ["jpg", "jpeg", "png"], accept_multiple_files = True)

if len(image) > 3:
    st.error("You can upload maximum 3 images")
else:
    if image:
       col = st.columns(len(image))
       for i, img in enumerate(image):
           with col[i]:
              st.image(img)