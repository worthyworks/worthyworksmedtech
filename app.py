import streamlit as st
from pathlib import Path
from PIL import Image

This_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR =This_DIR / "assets"
CONTACT_EMAIL = "info@worthy-works.com"
DEMO_VIDEO = "https://youtu.be/qZ9YYtWncgw"

  

st.set_page_config(page_title="Worthy Works MedTech",page_icon=":tada:", layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")  
#---Header
with st.container():
    st.subheader("Hi, I am Nimzing 👋🏾")
    st.title("A Physician From the United Kingdom")
    st.write("I am passionate about finding ways to use IT and Telehealth to improve care for patients globally!")
    st.write("[Learn More >](https://worthy-works.com)")
    
#--What I do
with st.container():
    st.write("---")
    left_column, mid_column, right_column= st.columns(3)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
           """
           On my YouTube channel, I create tutorials for people who:
           - are looking for a way to connect with a physician.
           - are seeking basic understanding about hepatitis and other liver diseases.
           - are seeking to learn how to use freely available resources to create learning resources.
           
           """ 
        )
        st.write("[Learn More >](https://www.youtube.com/@nimzing1)")
    with mid_column:
        st.header("What I Develop")
        st.write("##")
        st.write(
           """
           On the net, google and app stores, I have several apps, including:
           - EndoReportingApp
           - Abdominal pain checker.
           - Liver Health App.
           - Hepatitis Quizzer.
           - Liver Nutition
           - Hepatitis B Treatment | diets
           - Hepatitis e Book
           
           """ 
        )
        st.write("[Learn More >](https://play.google.com/store/apps/dev?id=4655352245010461881)")
        
    with right_column:
        st.header("Some evidence")
        st.write("##")
        product_image = Image.open(ASSETS_DIR / "appimag.png")
        st.image(product_image,width=225)
        
#--Projects
with st.container():
    st.write("---")
    st.header("Our Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        product_image = Image.open(ASSETS_DIR / "image1.png")
        st.image(product_image,width=300)
    with text_column:
        st.subheader("Use of a video-based app to report endoscopy")
        st.write(
            """
                Working with the BSG to pilot a simple but intuitive endoscopy reporting app.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/7TT9noiperY)")
        
with st.container():
    st.write("---")
    st.header("Our Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        product_image = Image.open(ASSETS_DIR / "wacp.png")
        st.image(product_image,width=300)
    with text_column:
        st.subheader("Development of a Web-based Continuing Medical Education Programmes")
        st.write(
            """
                Working with the West African College of Physicians to pilot a CME Programme.
                - Web-based
                - Combination of texts, files and videos
                - Quizzes embeded within each module
                - Beautiful certificate to those who complete the course
                - For several faculties
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/e_P9UlcHGq4)")
        
        
with st.container():
    st.write("---")
    st.header("Our Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        product_image = Image.open(ASSETS_DIR / "mansag.png")
        st.image(product_image,width=300)
    with text_column:
        st.subheader("Using Python/HTML/CSS to development membership management apps")
        st.write(
            """
                Working with the MANSAG - a Physician's Association in the UK to pilot a database for membership management.
                - Cloud-based
                - Adds members
                - Edits members
                - Searches members
                - Sends emails in bulk and individually to members
            """
        )
        
#--DEMO--
st.write("")
st.write("---")
st.subheader(":tv: Demo")
st.video(DEMO_VIDEO,format="video/mp4",start_time=0)
        
#---FAQ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")

faq = {
    "How can I access the video-based endoscopy reporting app?": 
        "The video-based endoscopy reporting app is currently being piloted with the British Society of Gastroenterology (BSG). You can access the app by visiting the BSG's website and following the instructions provided for the pilot program.",
    "Can you provide more information about the Web-based Continuing Medical Education Programmes?": 
        "The Web-based Continuing Medical Education (CME) Programmes, in collaboration with the West African College of Physicians, offer a flexible and interactive learning experience. These programs combine texts, files, and videos, and each module includes quizzes to reinforce learning. Participants who complete the course will receive a beautiful certificate. The CME Programmes cater to several faculties within the medical field.",
    "How do I join the membership management app developed for MANSAG?":
        "The membership management app developed for MANSAG, a Physician's Association in the UK, is cloud-based and designed to streamline membership-related tasks. To join, please visit the MANSAG website and follow the registration process to become a member. Once registered, you will have access to the app's features, including member management, email communication, and more.",
        
    "Is technical knowledge required to use the membership management app?": 
        "No, technical knowledge is not required to use the membership management app. The app is user-friendly and intuitive, designed to be accessible to admin members of MANSAG. You will find simple and straightforward options to add, edit, and search for members, as well as send bulk or individual emails to fellow members."
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)
        
#---CONTACT FORM--
st.write("")
st.write("---")
st.header(":mailbox: Have a Question? Ask Me Here!")
st.write("##")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit" class="button">Send 📧</button>
</form>
"""

lef_column, righ_column = st.columns(2)
with lef_column:
    st.markdown(contact_form,unsafe_allow_html=True)  
with righ_column:
    st.empty()    
        
