import streamlit as st
import pandas as pd

st.title("Dashboard page !!")

#for matrix
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

#json data
json_data = {"a": "1, 2, 3", "b": "4, 5, 6"}
st.json(json_data)

#to display code
code = """
print('hello world')
def func():
    return 0"""
st.code(code, language="python")

st.write("## H2 heading")   #can be used to write any kind of data

st.metric(label="Metric label", value="120m/s", delta="1.5m/s")

#dataframe and tables
table = pd.DataFrame({"Col1": [1, 2, 3, 4, 5], "Col2": [6, 7, 8, 9, 10]})
st.table(table)
st.dataframe(table)

#image
st.image("image.jpg", caption="Scenery Image", width=200)
#st.audio()
#st.video()

# dot(.) -- for accessing class
# hash(#) -- for accessing id
st.markdown("""
<style>
.st-emotion-cache-iiif1v.ef3psqc4
{
    visibility: hidden;
}
</style>       
""", unsafe_allow_html=True)

#checkbox
def changed():
    print("Changed")
    print(st.session_state.checker)     #session_state.key
state = st.checkbox("Checkbox", value=True, on_change=changed, key="checker")
if state:
    st.write("Hi")
else:
    pass

#radio button
radio_btn = st.radio("which Country ?", options=("US", "UK", "Canada"))
print(radio_btn)

#button
def btn_click():
    print("Button clicked !!")
btn = st.button("Click me", on_click=btn_click)

#select boxes & multiple select boxes
select = st.selectbox("Favourite Food ?", options=("Indian", "chinese", "Italian"))
print(select)
multi = st.multiselect("Favourite Food ?", options=("Indian", "chinese", "Italian"))
print(multi)
st.write(multi)