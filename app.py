import streamlit as st
from PIL import Image

#tab title
st.set_page_config(page_title="אלתרמן חלל ותעופה", page_icon=":school:", layout="wide")

#Top page image
image = Image.open(r"C:\Users\Maayan\Desktop\School Website\school.jpg")
st.image(r"C:\Users\Maayan\Desktop\School Website\school.jpg", caption='בית ספר לחלל ותעופה ע"ש אלתרמן', use_container_width=True)
