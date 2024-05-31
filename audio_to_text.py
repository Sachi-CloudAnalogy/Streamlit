import streamlit as st

st.markdown("<h1 style='text-align: center;'>----- Audio to Text Converter -----</h1>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)
audio = st.file_uploader("Upload your Audio File", type=['mp3', 'wav'])
