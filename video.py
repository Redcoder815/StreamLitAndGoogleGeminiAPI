import streamlit as st

video_file = st.file_uploader("Upload an video", type = ["mp4", "mkv"])

button = st.button("Click to upload")

if button:
    if video_file:
        st.video(video_file)
        st.success("Video uploaded successfully")
    else:
        st.error("Upload a video file")