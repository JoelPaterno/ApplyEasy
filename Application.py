import streamlit as st

st.title("Applications")

st.write("This is where you aply for jobs and track applciations")

st.text_input("Paste a job posting link from seek or linkedin here")
st.button("Apply", key="link_apply")

st.text_area("Paste a job application from anywhere here")
st.button("Apply", key="paste_apply")

#TODO - list job applications sorted by applied date. 