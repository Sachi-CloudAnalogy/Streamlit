import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="Web Scraper", page_icon=":performing_arts:", layout="wide")
st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Search with keyword")
    search = st.form_submit_button("Search")
placeholder = st.empty()

if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all("div", class_="d95fI")
    col1, col2 = placeholder.columns(2)
    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(4):
            img = figures[i].find("div", class_="WxXog").find("img")
            list = img['srcset'].split("?")
            anchor = figures[i].find("a", class_="Prxeh")
            if (i%2) == 0:
                col1.image(list[0], width=600)
                btn = col1.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com" + anchor['href'])

            else:
                col2.image(list[0], width=600)
                btn = col2.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com" + anchor['href'])
