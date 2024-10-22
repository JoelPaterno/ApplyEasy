import streamlit as st

pg = st.navigation([st.Page("src/ui/person_profile.py", title="Profile"), st.Page("src/ui/Application.py", title="Applications")])
pg.run()