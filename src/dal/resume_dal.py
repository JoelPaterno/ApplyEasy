from sqlalchemy.orm import Session
from database.models import Person, ResumeData, Skill, WorkExperience, Project, Certification, Reference

#CRUD + Get ResumeData methods
def create_resume(session: Session, personId: int, summary: str):
    """
    This method is used to create a new resumedata object.
    Args:

    Method calls:
        generate resume
    """
    pass

#CRUD + Get Work Experience methods
def create_work_experience(session: Session, resume_data: ResumeData, title: str, company: str, location: str, start_date: str, end_date: str, description: str):
    pass        

#CRUD + Get Projects methods
def create_project(session: Session, resume_data: ResumeData, name: str, description: str, link: str):
    pass    

#CRUD + Get Skill methods
def create_skill(session: Session, resume_data: ResumeData, skill: str):
    pass

#CRUD + Get certifications methods
def create_certification(session: Session, resume_data: ResumeData, name: str, link: str):
    pass

#CRUD + Get reference methods
def create_reference(session: Session, resume_data: ResumeData, name: str, title: str, company: str, email: str, phone: str):
    pass