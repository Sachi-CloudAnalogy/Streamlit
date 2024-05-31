import streamlit as st
import pandas as pd
import numpy as np
#to write
st.title("Title of the page")
st.subheader("Subheader")
st.header("Header")
st.text("it is used for Paragraph text")
st.markdown("**Bold**")      #for using design like html tags
st.markdown("*Italic*")
st.markdown(" # H1 heading ")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.caption("Caption")

st.write("Hello World !!")

#to take input
x = st.text_input("Today's date ?")     #for number, number_input
st.write(f"Today is {x}")

#buttons
button = st.button("Click")

#read data
data = pd.read_csv("data.csv")
st.write(data)

#creating graphs
chart = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.write(chart)
st.bar_chart(chart)
st.line_chart(chart)

#link to another page
st.link_button("Profile", url="/profile")
st.link_button("Dashboard", url="/dashboard")

#for deployment
#1 upload code on github
#2 make requirements.txt for dependencies
#3 click on deploy button in browser