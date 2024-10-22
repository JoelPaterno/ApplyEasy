import streamlit as st

def main():
  st.title("Applications")

  st.write("This is where you aply for jobs and track applciations")


  #initialise the session with data from the Person. 

  """
  Paste a link and get an applied for job. 

  Controllers
    - scrape the job posting
    - store the job application object in the database
    - generate job application docs
  """

  st.text_input("Paste a job posting link from seek or linkedin here")
  st.button("Apply", key="link_apply")


  """
  A text area to paste a job posting
  Controllers 
    - llm call to extract the job application from the job posting
    - store the job application object in the database
    - generate job application docs
  """
  st.text_area("Paste a job application from anywhere here")
  st.button("Apply", key="paste_apply")


  """
  List all job application sorted by date and jobs to apply for. 
  Controllers
    - get all job applications from the database. 
    - perform updates on the job application fields. 
    - re-run generate job application docs
  """

if __name__ == "__main__":
    main()