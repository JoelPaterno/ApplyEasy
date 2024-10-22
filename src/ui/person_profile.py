import streamlit as st
from src.controllers.profile_controller import create_new_person
from src.database.models import Person

def init_session():
    if 'person' not in st.session_state:
        st.session_state.person = None
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {
            'name': '',
            'email': '',
            'phone': '',
            'address': '',
            'website_name': '',
            'website_link': ''
        }


def main():
    init_session()

    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False

    # """
    # From a file upload, populate a person with resume data and all related objects. 

    # Controllers
    #     - populate person object from resume. 
    #     - generate cover letter
    # """
    with st.form("profile_form"):
        name = st.text_input("Name", key="name")
        email = st.text_input("Email", key="email")
        phone =st.text_input("Phone", key="phone")
        address = st.text_input("Address", key="address")
        website_name = st.text_input("website_name", key="website_name")
        website_link =st.text_input("website_link", key="website_link")
        submitted = st.form_submit_button("Submit")

        if submitted and not st.session_state.form_submitted:
            #call controller to create person object in db. 
            st.session_state.person = Person(name=name, email=email, phone=phone, address=address, website_name=website_name, website_link=website_link, resume_data=[], job_applications=[]), 
            create_new_person(st.session_state.person)
            st.session_state.form_submitted = True

    # """
    # show profile details
    # controllers
    # - show resume data
    # - add resume related objects
    # - edit and delete all personal details and resume data related details. 
    # """


if __name__ == "__main__":
    main()

