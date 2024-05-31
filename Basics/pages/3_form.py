import streamlit as st

#form
st.markdown("<h1 style='text-align: center;'>User Registration Form</h1>", unsafe_allow_html=True)
#way1
form = st.form("Form 1")
form.text_input("Name")
form.form_submit_button("Submit")

#way2
with st.form("Form 2", clear_on_submit=True):
    col1, col2 = st.columns(2)
    fname = col1.text_input("First Name")
    lname = col2.text_input("Last Name")
    email = st.text_input("Email Address")
    password = st.text_input("Password")
    cpassword = st.text_input("Confirm Password")
    d, m, y = st.columns(3)
    day = d.text_input("Day")
    month = m.text_input("Month")
    year = y.text_input("Year")
    state = st.form_submit_button("Submit")
    if state:
        if fname=="" or lname=="" or email=="" or password=="" or cpassword=="":
            st.warning("Please fill above fields !!")
        else:
            st.success("Submitted successfully !!")

