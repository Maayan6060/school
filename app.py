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
# st.markdown(
#     """
#     <style>
#     body {{
#         background-image: url('https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7');
#         background-size: 100% 80%; 
#         background-repeat: no-repeat;
#         background-position: center;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # image = Image.open("school.jpg")
# #st.image("https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7", caption='בית ספר לחלל ותעופה ע"ש אלתרמן', use_container_width=True)

import streamlit as st
import base64

# Set tab title
st.set_page_config(page_title="אלתרמן חלל ותעופה", page_icon=":school:", layout="wide")

# Function to encode image to Base64
def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded

# Convert the local image to Base64
image_path = "https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7"  # Replace with your image path
try:
    image_base64 = get_base64_image(https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7)
except FileNotFoundError:
    st.error(f"Image file '{https://www.netanya.muni.il/DocLib/%D7%97%D7%99%D7%A0%D7%95%D7%9A/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%A2%D7%9C%20%D7%99%D7%A1%D7%95%D7%93%D7%99/%D7%AA%D7%96/%D7%91%D7%99%D7%AA%20%D7%94%D7%A1%D7%A4%D7%A8%20%D7%9C%D7%AA%D7%A2%D7%95%D7%A4%D7%94%20%D7%95%D7%9C%D7%97%D7%9C%D7%9C%20%D7%A2%D7%9C%20%D7%A9%D7%9D%20%D7%90%D7%9C%D7%AA%D7%A8%D7%9E%D7%9F/28.jpg?RenditionID=7}' not found. Make sure it exists in the script directory.")

# Add CSS for background using Base64 image
if image_base64:
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url("data:image/jpg;base64,{image_base64}");
            background-size: 100% 80%;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add page content
st.title("ברוכים הבאים לבית ספר לחלל ותעופה ע\"ש אלתרמן")
st.subheader("דף זה נועד לעזור לכם ללמוד ולהתכונן למבחנים בצורה יעילה!")
