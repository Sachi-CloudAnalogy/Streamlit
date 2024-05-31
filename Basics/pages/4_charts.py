import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

#sidebars
st.sidebar.write("Hello, this is a sidebar.")
opt = st.sidebar.radio("Select any graph", options=("Line", "bar", "h-bar"))
if opt == "Line":
    st.markdown("<h1>Line Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    x = [0, 30, 45, 60, 90]
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.write(fig)
elif opt == "bar":
    st.markdown("<h1>Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    y = np.array([1, 2, 3, 4, 5])
    plt.bar(y, y*10)
    st.write(fig)
else:
    st.markdown("<h1>H-Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    y = np.array([1, 2, 3, 4, 5])
    plt.barh(y*10, y)
    st.write(fig)