import streamlit as st
import time
st.title("Profile Page !!")
st.markdown("---")   #draw line

#file upload
image = st.file_uploader("Label for file upload", type=["png", "jpg"], accept_multiple_files=False)
if image is not None:
    st.image(image)

#slider
st.slider("Slider", min_value=0, max_value=1000, value=500)

#text input
val = st.text_input("Enter name", max_chars=50)
print(val)

st.text_area("Description")
st.date_input("Enter date")
st.time_input("Time")
bar = st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    time.sleep(1)