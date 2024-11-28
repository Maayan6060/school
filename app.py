import streamlit as st
from PIL import Image

#tab title
#tab title
st.set_page_config(page_title="אלתרמן חלל ותעופה", page_icon=":school:", layout="wide")

#search engine optimization
st.markdown("""
      <meta name="google-site-verification" content="NMpko4mHDXRG7bRxWRz9ZaLISwNTjC3ckDQv3zPufI4" />
      <meta name="this is a school website. it contains information about the school, tests, assays, and exam dated for the students, custom AI to help students with multiple school subjexts and more" content="Alterman - A web app built using Streamlit">
      <meta name="Alterman" content="Alterman, Streamlit app, Web app, Example">
      <meta name="author" content="Your Name">
      <title>Alterman</title>
 """, unsafe_allow_html=True)

#Top page image
st.markdown(
    """
    <style>
    body {
        background-image: url('school.jpg');
        background-size: 100% 80%; 
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True

# image = Image.open("school.jpg")
# st.image("school.jpg", caption='בית ספר לחלל ותעופה ע"ש אלתרמן', use_container_width=True)
