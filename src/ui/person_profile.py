import streamlit as st

st.title("Profile")
st.write("This is a person profile page for setting up your profile")

"""
From a file upload, populate a person with resume data and all related objects. 

Controllers
    - populate person object from resume. 
    - generate cover letter
"""

st.file_uploader("Upload a Resume", type=["pdf", "docx"])

#TODO - Populate the session with the Person, Resume, and Cover Letter Data Objects. 

#initialise the session with data from person

"""
show profile details
controllers
    - show resume data
    - add resume related objects
    - edit and delete all personal details and resume data related details. 
"""
