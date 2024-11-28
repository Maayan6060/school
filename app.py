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
background_image_url = "https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: 100% 60%;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100vh;
    }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#horizontal image line
st.markdown(
    """
    <style>
    .horizontal-line {
        position: relative;
        width: 100%;
        height: 30px; 
        background-color: rgba(255, 255, 255, 0.9);
        margin: 20px 0; 
    }
    </style>
    <div class="horizontal-line"></div>
    """,
    unsafe_allow_html=True
)

# Streamlit content
st.title("Vertical Line Debug Example")
st.write("If you see this message, but not the vertical line, let's troubleshoot further!")
#image = Image.open("school.jpg")
#st.image("https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7", caption='בית ספר לחלל ותעופה ע"ש אלתרמן', use_container_width=True)

