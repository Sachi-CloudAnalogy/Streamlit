
# Streamlit web scrapper app

import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="Web Scraper", page_icon=":performing_arts:", layout="wide")
st.markdown("<h1 style='text-align: center;'>----- Web Scraper -----</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Search and download images with just a keyword!!</h2>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("What are you looking for ?")
    search = st.form_submit_button("Search")
placeholder = st.empty()

if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all("div", class_="d95fI")
    col1, col2, col3 = placeholder.columns(3)
    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(6):
            img = figures[i].find("div", class_="WxXog").find("img")
            list = img['srcset'].split("?")
            anchor = figures[i].find("a", class_="Prxeh")
            title = anchor["title"]
            if (i%2 != 0) and (i%3 != 0):
                col1.image(list[0], caption=title)
                btn = col1.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com" + anchor['href'])
            elif (i%2 == 0) and (i%3 != 0):
                col2.image(list[0], caption=title)
                btn = col2.button("Download", key=str(index) + str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com" + anchor['href'])
            else:
                col3.image(list[0], caption=title)
                btn = col3.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com" + anchor['href'])
