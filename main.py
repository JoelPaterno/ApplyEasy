import streamlit as st
from src.ui.person_profile import main as person_profile
from src.ui.Application import main as Applications

pg = st.navigation([
                    st.Page(person_profile, title="Profile", url_path="profile"), 
                    st.Page(Applications, title="Applications", url_path="applications")
                    ])
pg.run()