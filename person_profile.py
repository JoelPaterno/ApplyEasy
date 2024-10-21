import streamlit as st

st.title("Profile")
st.write("This is a person profile page for setting up your profile")

st.file_uploader("Upload a Resume", type=["pdf", "docx"])

#TODO - Populate the session with the Person, Resume, and Cover Letter Data Objects. 

