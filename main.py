import streamlit as st

pg = st.navigation([st.Page("person_profile.py", title="Profile"), st.Page("Application.py", title="Applications")])
pg.run()