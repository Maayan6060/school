# import streamlit as st
# from PIL import Image

# #tab title
# #tab title
# st.set_page_config(page_title="אלתרמן חלל ותעופה", page_icon=":school:", layout="wide")

# #search engine optimization
# st.markdown("""
#       <meta name="google-site-verification" content="NMpko4mHDXRG7bRxWRz9ZaLISwNTjC3ckDQv3zPufI4" />
#       <meta name="this is a school website. it contains information about the school, tests, assays, and exam dated for the students, custom AI to help students with multiple school subjexts and more" content="Alterman - A web app built using Streamlit">
#       <meta name="Alterman" content="Alterman, Streamlit app, Web app, Example">
#       <meta name="author" content="Your Name">
#       <title>Alterman</title>
#  """, unsafe_allow_html=True)

# #Top page image
# background_image_url = "https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7"
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url("{background_image_url}");
#         background-size: 100% 80%; 
#         background-repeat: no-repeat; 
#         background-position: center; 
#         background-attachment: scroll; 
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )



# #horizontal image line+text
# st.markdown(
#     """
#     <style>
#     .horizontal-line {
#         position: relative;
#         right: 1000px;
#         width: 200%;
#         height: 80px; 
#         background-color: rgba(255, 255, 255, 0.75);
#         margin: 20px 0; 
#         z-index: 1000;
#     }
#     .line-text {
#        position: absolute;
#        top: 50%; 
#        left: 50%; 
#        transform: translate(-50%, -50%);
#        font-size: 60px; 
#        color: #001f3f;
#        font-family: 'BN Cloud'; 
#     }
#     </style>
#     <div class="horizontal-line">
#     <div style="position: relative; z-index: 1000;">
#        <div class="line-text">חטיבת ביניים חלל ותעופה ע"ש אלתרמן</div>
#     </div>

#     """,
#     unsafe_allow_html=True
# )

# #Text - paragraph 1
# st.markdown(
#     """
#     <style>
#     .custom-text {
#         position: relative;
#         bottom: -10000px; 
#         left: 50px; 
#         font-size: 20px; 
#         color: black;
#     }
#     </style>
#     <div class="custom-text">
#         rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr.
#     </div>
#     """,
#     unsafe_allow_html=True
# )

import streamlit as st
from PIL import Image

# Tab title
st.set_page_config(page_title="אלתרמן חלל ותעופה", page_icon=":school:", layout="wide")

# Search engine optimization
st.markdown(
    """
      <meta name="google-site-verification" content="NMpko4mHDXRG7bRxWRz9ZaLISwNTjC3ckDQv3zPufI4" />
      <meta name="this is a school website. it contains information about the school, tests, assays, and exam dated for the students, custom AI to help students with multiple school subjexts and more" content="Alterman - A web app built using Streamlit">
      <meta name="Alterman" content="Alterman, Streamlit app, Web app, Example">
      <meta name="author" content="Your Name">
      <title>Alterman</title>
     """,
    unsafe_allow_html=True
)

# Top page image
background_image_url = "https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: 100% 80%; 
        background-repeat: no-repeat; 
        background-position: center; 
        background-attachment: scroll; 
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Horizontal image line + text
st.markdown(
    """
    <style>
    .horizontal-line {
        position: relative;
        right: 1000px;
        width: 200%;
        height: 80px; 
        background-color: rgba(255, 255, 255, 0.75);
        margin: 20px 0; 
        z-index: 1000;
    }
    .line-text {
       position: absolute;
       top: 50%; 
       left: 50%; 
       transform: translate(-50%, -50%);
       font-size: 60px; 
       color: #001f3f;
       font-family: 'BN Cloud'; 
    }
    </style>
    <div class="horizontal-line">
    <div style="position: relative; z-index: 1000;">
       <div class="line-text">חטיבת ביניים חלל ותעופה ע"ש אלתרמן</div>
    </div>

    """,
    unsafe_allow_html=True
)

# Text - paragraph 1
st.markdown(
    """
    <style>
    .custom-text {
        position: absolute;
        margin-top: 10000px;
        font-size: 20px; 
        color: black;
    }
    </style>
    <div class="custom-text">
        rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr.
    </div>
    """,
    unsafe_allow_html=True
)






