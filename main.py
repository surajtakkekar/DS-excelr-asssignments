import streamlit as st
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pyresparser import ResumeParser
import pdftotext
import nltk
import pdf
import pdfminer
from pdfminer.high_level import extract_pages
import parser
from PIL import Image
from extraction import ResumeParser
parser = ResumeParser()

img = Image.open('dog_PNG50322.png')
img = img.resize((250, 180))
st.image(img)




st.sidebar.title("Resume Deployment")
resume=st.sidebar.file_uploader("PROJECT 113",type=["pdf"])
# print(dir(resume))
if st.sidebar.button("Upload"):

    if resume is not None:
        # with open(resume.getvalue(), "rb") as f:
        pdf = pdftotext.PDF(resume)
        finalpg=''
        for i in pdf or []:

            pg=i.strip()
            finalpg+=pg
        st.write("NAME: ",parser.extract_name(finalpg))
        st.write("CONTACT: ", parser.extract_phone_number(finalpg))
        st.write("EMAIL: ", str(parser.extract_email(finalpg)))
        st.write("LINKEDIN: ", str(parser.extract_linkedin(finalpg)))
        st.write("GITHUB: ", str(parser.extract_github(finalpg)))
        st.write("EDUCATION: ", str(parser.extract_text(finalpg)))
        st.write("EXPERIENCE: ", str(parser.extract_experience(finalpg)))
        st.write("HOBBIES: ", str(parser.extract_hobby(finalpg)))
        st.write("LANGUAGES: ", str(parser.extract_language(finalpg)))
        st.write("LOCATION: ", str(parser.locationExtraction(finalpg)))
    else:
        st.error("Please select a PDF file!")
st.sidebar.text("Made with ❤️ by Team DANNY AND GEERATH "
                "SURAJ AND KEDAR "
                "RUSHI AND  RAKHI,  Searce Inc.")